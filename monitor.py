import mysql.connector
import time
from playsound import playsound
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def check_for_slow_queries():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT 
        'Current Slow Queries' as metric_type,
        COUNT(*) as count,
        AVG(time) as avg_duration,
        MAX(time) as max_duration
    FROM INFORMATION_SCHEMA.PROCESSLIST
    WHERE command = 'Query' AND time > 2 
    UNION ALL 
    SELECT 
        'Long Running Connections',
        COUNT(*) as count,
        AVG(time) as avg_duration,
        MAX(time) as max_duration
    FROM INFORMATION_SCHEMA.PROCESSLIST
    WHERE command = 'Sleep' AND time > 300;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"{row['metric_type']}: Count={row['count']}, Avg={row['avg_duration']}, Max={row['max_duration']}")

    # Alert if slow queries present
    if results[0]['count'] > 0:
        print("🚨 ALERT: Slow query detected!")
        playsound('alert_sound.mp3')
        show_executing_queries()

    cursor.close()
    conn.close()

def show_executing_queries():
    print("\n🔍 Executing Queries:")
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SHOW PROCESSLIST")

    rows = cursor.fetchall()
    executing_queries = [
        row for row in rows if row['Command'] == 'Query' and (row['State'] or '').lower() == 'executing'
    ]

    if executing_queries:
        for row in executing_queries:
            print(f"ID: {row['Id']}, User: {row['User']}, Host: {row['Host']}, DB: {row['db']}, Time: {row['Time']}")
            print(f"State: {row['State']}, Info: {row['Info']}")
            print("-" * 80)
    else:
        print("No queries currently executing.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("🔍 MySQL Slow Query Monitor Started")
    while True:
        try:
            check_for_slow_queries()
        except Exception as e:
            print("[ERROR]", e)
        time.sleep(30)  # Check every 1 minute

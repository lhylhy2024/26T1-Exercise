import sqlite3


def simple_query():
    """简单查询示例"""
    # 连接到数据库
    conn = sqlite3.connect('rates.db')
    cursor = conn.cursor()

    print("汇率数据库查询工具")
    print("=" * 40)

    # 查询所有数据
    cursor.execute("SELECT * FROM rates")
    rows = cursor.fetchall()

    # 显示数据
    print(f"\n共找到 {len(rows)} 种货币:\n")
    print(f"{'货币':<10} {'TSP':<10} {'CSP':<10} {'TBP':<10} {'CBP':<10}")
    print("-" * 50)

    for row in rows:
        print(f"{row[0]:<10} {row[1]:<10.2f} {row[2]:<10.2f} {row[3]:<10.2f} {row[4]:<10.2f}")

    # 查询特定货币
    currency = input("\n输入要查询的货币名称 (直接回车退出): ")
    if currency:
        cursor.execute("SELECT * FROM rates WHERE Currency = ?", (currency,))
        result = cursor.fetchone()

        if result:
            print(f"\n查询结果 - {currency}:")
            print(f"现汇卖出价(TSP): {result[1]:.2f}")
            print(f"现钞卖出价(CSP): {result[2]:.2f}")
            print(f"现汇买入价(TBP): {result[3]:.2f}")
            print(f"现钞买入价(CBP): {result[4]:.2f}")
        else:
            print(f"未找到货币: {currency}")

    # 关闭连接
    conn.close()
    print("\n查询完成!")


if __name__ == "__main__":
    simple_query()
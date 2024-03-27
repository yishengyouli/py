months_budget = []
# 收集12个月的预算值
for i in range(1, 13):
    print(f"请输入第{i}月的预算（小于350的非负整数）：", end='')
    budget = int(input())
    months_budget.append(budget)

current_money = 0  # 当前手中的钱
saved_money = 0  # 存储在妈妈那里的钱
deficit_total = 0  # 记录因资金不足而超出的总金额

for month, budget in enumerate(months_budget, start=1):
    current_money += 300  # 每月开始时，津津得到300元零花钱
    if current_money < budget:
        deficit = current_money - budget  # 计算超出的金额
        print(f"第{month}月，超出: {deficit}")
        deficit_total += deficit  # 累加到总超出金额
        current_money = 0  # 假设津津能够通过其他方式调整，这个月结束时手中无余额
    else:
        current_money -= budget  # 扣除当月预算
    # 如果月末剩余超过100元，则存整百金额
    saved_this_month = (current_money // 100) * 100
    saved_money += saved_this_month
    current_money -= saved_this_month

# 计算年末总金额：手中的钱 + 储蓄加20%的利息 - 因资金不足而超出的总金额
total_money = current_money + saved_money * 1.2 + deficit_total
print(f"年终总资金（包括超出部分）: {total_money}")

# Manual process cost
manual_cost = 50000

# Automation cost
automation_cost = 15000

# Savings calculation
savings = manual_cost - automation_cost

# ROI calculation
roi = (savings / automation_cost) * 100

# Output
print("===== ROI ANALYSIS =====")
print("Manual Cost:", manual_cost)
print("Automation Cost:", automation_cost)
print("Savings:", savings)
print("ROI:", round(roi, 2), "%")
from calculations import calculate_static_margin
from visualization import draw_rocket

print("[Rocket Stability Calculator]")

length = float(input("Enter the rocket length (m): "))
cg = float(input("Enter the center of gravity (m): "))
cp = float(input("Enter the center of pressure (m): "))
diameter = float(input("Enter the rocket diameter (m): "))

margin = calculate_static_margin(cg, cp, diameter)

# Determine rocket stability
if margin >= 1:
    status = "STABLE"
elif margin > 0:
    status = "MARGINALLY STABLE"
else:
    status = "UNSTABLE"

# Draw the rocket visualization
draw_rocket(length, cg, cp, margin, status)

print("\n-----Results-----")
print(f"Static Margin = {margin:.2f} calibers")
print(f"Status        : {status}")
from gauges import *
from config import programConfig

def compileGauges():
	gauges = [] 
	# "0CFFF048" --- rpm
	# "0CFFF148" --- Barometer
	# "0CFFF050" --- TPS
	# "0CFFF150" --- map
	# "0CFFF052" --- Fuel Open Time
	# "0CFFF054" --- Ignition Angle
	# "0CFFF152" --- Lambda
	# "0CFFF154" --- Pressure Type
	# "0CFFF248" --- Analog Input 1
	# "0CFFF250" --- Analog Input 2
	# "0CFFF252" --- Analog Input 3
	# "0CFFF254" --- Analog Input 4
	# "0CFFF348" --- Analog Input 5
	# "0CFFF350" --- Analog Input 6
	# "0CFFF352" --- Analog Input 7
	# "0CFFF354" --- Analog Input 8
	# "0CFFF448" --- Frequency 1
	# "0CFFF450" --- Frequency 2
	# "0CFFF452" --- Frequency 3
	# "0CFFF454" --- Frequency 4
	# "0CFFF548" --- Battery Voltage
	# "0CFFF550" --- Air Temp
	# "0CFFF552" --- Coolant Temp
	# "0CFFF554" --- Temp Type
	# "0CFFF648" --- Analog Input 5 - Thermistor
	# "0CFFF650" --- Analog Input 6 - Thermistor
	# "0CFFF652" --- Version Major
	# "0CFFF654" --- Version Minor
	# "0CFFF656" --- Version Build
	# "0CFFF658" --- TBD

	# declare gauge or view here
	# declaring just means gauges.append("name of gauge class you write"())
	#
	# your code starts here
	gauges.append(circularGauge(390, 100, 500, 500, "0CFFF048", startAngle = 45, color=programConfig.barColor, fontcolor=programConfig.fontColor))
	gauges.append(circularGauge(50, 420, 300, 300, "0CFFF050", startAngle = 45, color=programConfig.barColor, fontcolor=programConfig.fontColor))
	gauges.append(circularGauge(920, 420, 300, 300, "0CFFF548", startAngle = 45, color=programConfig.barColor, fontcolor=programConfig.fontColor))
	gauges.append(textGauge(1280, 10, "0CFFF048", "0CFFF148", "0CFFF050", "0CFFF150", "0CFFF052", "0CFFF658", "0CFFF656", 
		"0CFFF654", "0CFFF652", "0CFFF650", "0CFFF648", "0CFFF554", "0CFFF552", "0CFFF550", fontSize=10, fontcolor=programConfig.fontColor))
	gauges.append(textGauge(1070, 10, "0CFFF548", "0CFFF454", "0CFFF452", "0CFFF450", "0CFFF448", "0CFFF354",
	"0CFFF352", "0CFFF350", "0CFFF348", "0CFFF254", "0CFFF252", "0CFFF250", "0CFFF248", fontSize=10, fontcolor=programConfig.fontColor))
	gauges.append(barGauge(530, 500, 250, 50, "0CFFF048", "0CFFF054", padding=20, color=programConfig.barColor, fontcolor=programConfig.fontColor))
	gauges.append(barGauge(50,100, 50, 250, "0CFFF552", "0CFFF050", orientation=barGauge.VERTICAL, padding=20, color=programConfig.barColor, fontcolor=programConfig.fontColor))
	# your code stops here

	return gauges
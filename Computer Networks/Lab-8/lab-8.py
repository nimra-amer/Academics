import ns.core
import ns.network
import ns.internet
import ns.point_to_point
import ns.applications

# Enable logging for UDP echo client and server applications
ns.core.LogComponentEnable("UdpEchoClientApplication", ns.core.LOG_LEVEL_INFO)
ns.core.LogComponentEnable("UdpEchoServerApplication", ns.core.LOG_LEVEL_INFO)

# Create two nodes
nodes = ns.network.NodeContainer()
nodes.Create(2)

# Set up point-to-point link with data rate of 5 Mbps and 2 ms delay
pointToPoint = ns.point_to_point.PointToPointHelper()
pointToPoint.SetDeviceAttribute("DataRate", ns.core.StringValue("10Mbps"))
pointToPoint.SetChannelAttribute("Delay", ns.core.StringValue("5ms"))

# Install network devices on the nodes
devices = pointToPoint.Install(nodes)

# Install the internet stack on the nodes
stack = ns.internet.InternetStackHelper()
stack.Install(nodes)

# Assign IP addresses to the network devices
address = ns.internet.Ipv4AddressHelper()
address.SetBase(ns.network.Ipv4Address("10.1.1.0"), ns.network.Ipv4Mask("255.255.255.0"))
interfaces = address.Assign(devices)

# Set up the UDP echo server on Node 1 (second node)
echoServer = ns.applications.UdpEchoServerHelper(8080)
serverApps = echoServer.Install(nodes.Get(1))
serverApps.Start(ns.core.Seconds(1.0))
serverApps.Stop(ns.core.Seconds(10.0))

# Set up the UDP echo client on Node 0 (first node)
echoClient = ns.applications.UdpEchoClientHelper(interfaces.GetAddress(1), 8080)
echoClient.SetAttribute("MaxPackets", ns.core.UintegerValue(5))
echoClient.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds(0.5)))
echoClient.SetAttribute("PacketSize", ns.core.UintegerValue(512))

clientApps = echoClient.Install(nodes.Get(0))
clientApps.Start(ns.core.Seconds(2.0))
clientApps.Stop(ns.core.Seconds(10.0))

# Run the simulation
ns.core.Simulator.Run()
ns.core.Simulator.Destroy()

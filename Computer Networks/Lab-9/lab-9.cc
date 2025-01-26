#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"

using namespace ns3;

int main(int argc, char *argv[]) {
    Time::SetResolution(Time::NS);

    NodeContainer networkNodes;
    networkNodes.Create(4);

    PointToPointHelper link1, link2, link3;
    link1.SetDeviceAttribute("DataRate", StringValue("2Mbps"));
    link1.SetChannelAttribute("Delay", StringValue("10ms"));

    link2.SetDeviceAttribute("DataRate", StringValue("2Mbps"));
    link2.SetChannelAttribute("Delay", StringValue("10ms"));

    link3.SetDeviceAttribute("DataRate", StringValue("1.7Mbps"));
    link3.SetChannelAttribute("Delay", StringValue("20ms"));

    NetDeviceContainer devices1, devices2, devices3;
    devices1 = link1.Install(networkNodes.Get(0), networkNodes.Get(2));
    devices2 = link2.Install(networkNodes.Get(1), networkNodes.Get(2));
    devices3 = link3.Install(networkNodes.Get(2), networkNodes.Get(3));

    InternetStackHelper stackHelper;
    stackHelper.Install(networkNodes);
    Ipv4AddressHelper addressHelper1, addressHelper2, addressHelper3;
    addressHelper1.SetBase("10.1.1.0", "255.255.255.0");
    addressHelper2.SetBase("10.1.2.0", "255.255.255.0");
    addressHelper3.SetBase("10.1.3.0", "255.255.255.0");

    Ipv4InterfaceContainer interfaces1, interfaces2, interfaces3;
    interfaces1 = addressHelper1.Assign(devices1);
    interfaces2 = addressHelper2.Assign(devices2);
    interfaces3 = addressHelper3.Assign(devices3);


    uint16_t tcpPort = 8080;
    uint16_t udpPort = 9090;
    Address tcpSinkAddress(InetSocketAddress(interfaces3.GetAddress(1), tcpPort));
    PacketSinkHelper tcpSinkHelper("ns3::TcpSocketFactory", tcpSinkAddress);
    ApplicationContainer sinkAppTcp = tcpSinkHelper.Install(networkNodes.Get(3));
    sinkAppTcp.Start(Seconds(0.0));
    sinkAppTcp.Stop(Seconds(5.0));

    Ptr<Socket> tcpSocket = Socket::CreateSocket(networkNodes.Get(1), TcpSocketFactory::GetTypeId());
    OnOffHelper tcpOnOff("ns3::TcpSocketFactory", tcpSinkAddress);
    tcpOnOff.SetAttribute("DataRate", StringValue("1Mbps"));
    tcpOnOff.SetAttribute("PacketSize", UintegerValue(1024));
    tcpOnOff.SetAttribute("StartTime", TimeValue(Seconds(0.5)));
    tcpOnOff.SetAttribute("StopTime", TimeValue(Seconds(4.0)));

    ApplicationContainer tcpClientApp = tcpOnOff.Install(networkNodes.Get(1));

    Address udpSinkAddress(InetSocketAddress(interfaces3.GetAddress(1), udpPort));
    PacketSinkHelper udpSinkHelper("ns3::UdpSocketFactory", udpSinkAddress);
    ApplicationContainer sinkAppUdp = udpSinkHelper.Install(networkNodes.Get(3));
    sinkAppUdp.Start(Seconds(0.0));
    sinkAppUdp.Stop(Seconds(5.0));

    OnOffHelper udpOnOff("ns3::UdpSocketFactory", udpSinkAddress);
    udpOnOff.SetAttribute("DataRate", StringValue("100Kbps"));
    udpOnOff.SetAttribute("PacketSize", UintegerValue(1024));
    udpOnOff.SetAttribute("StartTime", TimeValue(Seconds(0.1)));
    udpOnOff.SetAttribute("StopTime", TimeValue(Seconds(4.5)));

    ApplicationContainer udpClientApp = udpOnOff.Install(networkNodes.Get(0));
    link1.EnablePcapAll("link1");
    link2.EnablePcapAll("link2");
    link3.EnablePcapAll("link3");

    Simulator::Run();
    Simulator::Destroy();

    return 0;
}

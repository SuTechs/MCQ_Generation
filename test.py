from app.mcq_generation import MCQGenerator

text = '''
The history of natural language processing (NLP) generally started in the 1950s,
although work can be found from earlier periods. In 1950, Alan Turing published 
an article titled "Computing Machinery and Intelligence" which proposed what is 
now called the Turing test as a criterion of intelligence. The Georgetown experiment 
in 1954 involved fully automatic translation of more than sixty Russian sentences 
into English. The authors claimed that within three or five years, machine translation 
would be a solved problem. However, real progress was much slower, and after the ALPAC 
report in 1966, which found that ten-year-long research had failed to fulfill the 
expectations, funding for machine translation was dramatically reduced. Little further 
research in machine translation was conducted until the late 1980s when the first statistical 
machine translation systems were developed.
'''

long_text = '''
What is computer Network?
A communication system for connecting computers/hosts.
•A computer network is a number of  computers ( also known as nodes) connected by some communication lines.
•Two computers connected to the network can communicate with each other through the other nodes if they are not directly connected.
•Some of the nodes in the network may not be computers at all but they are network devices( Like switches, routers etc.) to facilitate the communication.

Uses of the computer Network
•Exchange of information between different computers. (File sharing)
•Interconnected small computers in place of large computers.
•Communication tools (voice , video)
•Some applications and technologies are examples of Distributed system. (Railway reservation system, Distributed databases etc).

Advantages of Computer Network?
•Better communication
•Better connectivity
•Better sharing of Resources
•Bring people together

Network supporting the way we live
Communication is almost as important to us as our reliance on air, food, water and shelter. The methods that we used to share the information are constantly changing and evolving. As with every advance in communication technology, the creation and interconnection of data network is having a profound effect. These days computer networks have evolved to carry voice, video streams, text and graphics between many different types of devices.

The immediate nature of communications over the Internet encourages the formation of global communities. These communities foster social interaction that is independent of location or time zone.
Examples of Todays popular communication tools.
1.Instant messaging
2.Weblogs
3.wikis
4.Podcasting
5.Collaboration tools
6.Facebook
7.Twitter
Networks Supporting the way we learn
communication, collaboration and engagement are fundamental building blocks of education. institutions are

continually striving to enhance these processes to maximize the dissemination of knowledge. Robust and reliable networks support and enrich student learning experiences.
Traditional Learning Process:
1.Text book
2.Instructor
these are limited in type of format and the timing of the presentation.In contrast, on-line courses can contain voice, data, and video, and are available to the students at any time from any place. on line distance learning has removed geographic barriers and improved student opportunity.
•course-ware
•collaboration
•References
•Administration
Network supporting the way we work:
Remote Access: Business application can be accessed remotely as if employees were on site.
Multiple Resources: workers in any location can reach each other and access multiple resources on the network.

Network supporting the way we play:
on-line games

Types of Computer Network:

LAN	WAN


Faster Cheaper
Under a control of single ownership.
Typical Speeds:
10 Mbps to l0Gbps

Slower Expensive
Not under a control of a single person.
Typical Speed:
64 Kbps to 8 Mbps





Historical Events:
•1948 first commercial computer installed UNIVAC 1
•1958 First U.S communication satellite.
•1964 SABRE airline reservation system packet switching network (Proposed by RAND).
•1969 ARPANET first packet switching network beings operation.
•1971 frist computer chip
-4 bit, 2,300 transistors
•1972 Ethernet specifications forumulated
•1974 introduces SNA
•1975 Altair 8800 first commercial micocomputer sold as kit.
•1975 Paul Allan/Bill Gates wrote a BASIC language interpreter for the Altair, they formed Microsoft.

•1976 Wozniak and jobs built Apple I and formed Apple computer company.
•1979 Visicalc first commercial spread sheet introduced.
•1981 IBM introduces IBM PC one floppy
•1983 TCP/IP becomes the official protocol on ARPANET.
•1984 Apple introduced GUI with Apple Macintosh.
•1986 Laptop PC.

Modes of communication:
In an IPv4 network, the hosts can communicate one of three different ways:
Unicast - the process of sending a packet from one host to an individual host Broadcast - the process of sending a packet from one host to all hosts in the network Multicast - the process of sending a packet from one host to a selected group of hosts




Protocol:
A protocol defines the format and the order of messages exchanged between two or more
•Each protocol object has two different interfaces.
-Service interfaces: Defines operation on this protocol.
-Peer-to-peer interfaces: Defines message exchanged with peer.
communicating entities, as well as the actions taken on the transmission and/or receipt of a message.
•Building blocks of a Network Architecture.


•Most networks are organized as a series of layers.
•The task of each layer is to give some service to the upper layers.
•Any layer maintains a virtual connection with the corresponding layer in a peer.
•There is a peer to peer protocol running between any two corresponding layers.
•The interface between any two layers is well defined.
•The implementation of each layer in each node is transparent to other devices.



A Human protocol and Computer Network protocol

Principle of Communication:






The primary purpose of any network is to provide a method to communicate. All communication methods have three elements in common. The first of these elements is the message source, or sender. Message sources are people, or electronic devices, that need to communicate a message to other individuals or devices. The second element of communication is the destination, or receiver, of the message. The destination receives the message and interprets it. A third element, called a channel, provides the pathway over which the message can travel from source to destination.


Protocols are specific to the characteristics of the source, channel and destination of the message. The rules used to communicate over one medium, like a telephone call, are not necessarily the same as communication using another medium, such as a letter.

'''

count = 2

questions = MCQGenerator().generate_mcq_questions(text, count)
result = [q.__dict__ for q in questions]

print('----------GENERATED QUESTIONS----------')
for q in result:
    print(q)

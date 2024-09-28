#A vendor offers software services to a client. Each resource is billed at some dollar rate per hour. 
# The total cost of the project for the client is therefore, the total number of hours contributed by all the vendor resources * the dollar rate / hour. 
# There are however some variants.
#  a. The vendor might have purchased hardware/infrastructure or software licenses needed for the project. 
# b. The vendor might have utilized external consultants for the project. 
# c. The client looks at the vendor as a one stop solution and hence external resources employed by the vendor need to be paid by the vendor.
#  d. It might however be possible that the vendor’s hardware and software purchases are borne by the client. In this case, the client pays the vendor 30% of the hardware/infrastructure costs. In case of software licenses, the client pays the vendor 50% of the cost, if they are commonly available and used, or 100% if the software is infrequently used or is proprietary client technology.

#  e. The external consultants employed by the vendor will come at a dollar rate per hour. 
# f.  Accept the suitable inputs and display the profits / loss realized by the vendor.
#
def BasicRate(Htime,Stime,ExtTime,Costperhr):
    hardware_cost=0
    software_cost=0
    ext_consul_cost=0
    if Htime!=0:
        hardware_cost=(Htime*Costperhr)*.3
    if Stime!=0:
        Typeofsoftware=int(input('''
If Commonly used software used Enter "0"
If Software used Infrequently  Enter "1"
If Both used Enter "2"                                               
'''))
        if Typeofsoftware==0:
            software_cost=(Stime*Costperhr)*.5
        elif Typeofsoftware==1:
            software_cost=Stime*Costperhr
        elif Typeofsoftware==2:
            software_cost=(Stime*Costperhr)*1.5
    if ExtTime!=0:
        ext_consul_cost=ExtTime*Costperhr
    print(f'The Cost realised by the vendor is ${(hardware_cost+software_cost+ext_consul_cost)}')

time_hardware=int(input('Time taken for hardware: '))
time_software=int(input('Time taken for software required: '))
time_extconsuls=int(input('Time taken for external consultants: '))
CPHr=int(input('Cost per hr: '))
BasicRate(time_hardware,time_software,time_extconsuls,CPHr)

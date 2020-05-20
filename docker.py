import os

import sys, tty,termios


os.system("tput setab 54")
print("\t\t\twelcome to my docker world")
os.system("tput setaf 9")
print("\t\t\t--------------------------")


print("where u want to prerform ur job (local/remote) : " , end="")
location = input()
print(location)



if location == "remote":

    remoteIP = input("plz enter ur IP address : ")

while True:
        print("""
        print1: To pull(download) any image
        print2: To push(uplaod) any image
        press3: To start a container
        press4: To setup ur network
        press5: To launch a container using ur network
        press6: To exit 
              """)

        print("enter ur choice : " , end="")
        ch=input()
        print(ch)

        if location == "local":
          
            
            if int(ch) == 1:
                print("can u plzz tell me ur image name: " , end="")
                dimage_name = input()

                os.system("docker pull  {} "  .format(dimage_name))      
            

            elif int(ch) == 2:
                print("can u plzz tell me ur image name :" , end="")
                uimage_name = input()

                print("can u plzz tell me ur docker id :" , end="")
                docker_id = input()

                os.system("docker push {}/{}" .format(docker_id , uimage_name))

            
            elif int(ch) == 3:
                print("can u plzz tell me ur container name: " , end="")
                container_name = input()

                os.system("docker run -it --name {} prit0541/mydocker:1 "  .format(container_name))


            elif int(ch) == 4:
                print("can u plzz tell me ur network name: " , end="")
                nat_name = input()

                os.system("docker network create --driver bridge {}" .format(nat_name))

        
            elif int(ch) == 5:
                print("can u plzz tell me ur network name: " , end="")
                nat_name = input()

                print("can u plzz tell me ur container name: " , end="")
                cantr_name = input()


                os.system("docker run -it --name {} --network {} prit0541/mydocker:1 " .format(cantr_name , nat_name) )

            elif int(ch) == 6:
                exit()

            else:
                print("option not supported")
        input("enter to continue>>>>:::::--->")
        os.system("clear")


        if location == "remote":


            if int(ch) == 1:
                print(" can u plzz tell me ur image name: " , end="")
                dimage_name = input()

                os.system(" ssh {0} docker pull  {1} "  .format(remoteIP , dimage_name))


            if int(ch) == 3:
                print("can u plzz tell me ur container name: " , end="")
                container_name = input()

                os.system("ssh {0} docker run -i --name {1} prit0541/mydocker:1 "  .format(remoteIP , container_name))


            elif int(ch) == 4:
                print("can u plzz tell me ur network name: " , end="")
                nat_name = input()

                os.system("ssh {0} docker network create --driver bridge {1}" .format(remoteIP , nat_name))

        
            elif int(ch) == 5:
                print("can u plzz tell me ur network name: " , end="")
                nat_name = input()

                print("can u plzz tell me ur container name: " , end="")
                cantr_name = input()


                os.system("ssh {0} docker run -i --name {1} --network {2} prit0541/mydocker:1 " .format(remoteIP , cantr_name , nat_name) )

            
            elif int(ch) == 6:
                exit()

            else:
                print("option not supported")
        input("enter to continue>>>>:::::--->")
        os.system("clear")


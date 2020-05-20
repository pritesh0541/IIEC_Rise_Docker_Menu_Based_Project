# IIEC_Rise_Docker_Menu_Based_Project
  Under the IIEC_RISE 1.0 Campaign I learnt about Docker Under The World Record Holder Mr. Vimal Daga sir . This is my final project  to make docker working easy using menu based approach.

## Explanation of whole set-up of this project:-

### 1. Some basic configuration:-
 *  I am using RedHat Enterprise linux Version 8 , also having pre-installed Docker software .

     * Start Dockor services:-
     
          * Use systemctl start docker
          
### 2. Some basic requierments:-        
 *  Disable firewalld services:-
                              
       *  Firewalld might block some networking stuf's that's why needed to stop firewalld services.
      
          * Use systemctl stop firewalld
          

### 3. Download required images:-
 * This is very important phase of this project .You must have a Docker image which is used in this project. The required image must be  exist in both local and remote system.
                         
     * To download docker images:-
          
         * use docker pull <image name>
  
     * This project required image:-
     
         * Use docker pull prit0541/mydocker:1

![Redhat 8  Running  - Oracle VM VirtualBox screenshot 0](https://user-images.githubusercontent.com/64368194/82417414-259de500-9a99-11ea-9127-0e939a630805.png)



# Note:- 
       You can also download any image using this project.
       
       
# working:-


  ## 1. I have created a root directory pritesh.

  ## 2. In this pritesh (directory) i have created a docker.py folder which is having all the coding.

  * {dot}.py because i am using python language in this project.

  * Go inside the pritesh directory to run your project:-
              
       * python3 docker.py
  
![Redhat 8  Running  - Oracle VM VirtualBox screenshot1](https://user-images.githubusercontent.com/64368194/82422167-b972af80-9a9f-11ea-98ae-0963beb49254.png)


 * In this project i am having two parts.

# A:- local system:-
                In this the project is work on your local system.
                

## 1. This is use to pull any Docker images from docker hub:- 

  ![Redhat 8  Running  - Oracle VM VirtualBox screenshot 2 (2)](https://user-images.githubusercontent.com/64368194/82423141-03a86080-9aa1-11ea-9caa-b450b82a14a4.png)
    

## 2. This is use to push the docker images from your local system to docker hub to publish your image:- 

![Redhat 8  Running  - Oracle VM VirtualBox screenshot 3](https://user-images.githubusercontent.com/64368194/82423361-48cc9280-9aa1-11ea-84ab-e991aee430bb.png)

# note:- 
* If you want to push any image to docker hub then first you have to loggin to your docker hub on your host using your docker-id and docker hub password . 
   
   * use docker login 
            
     docker-id:- (your docker id )
            
     password:- (your docker hub password)
       
       
## 3. This is use to launch a container using your own name:-

![Redhat 8  Running  - Oracle VM VirtualBox screenshot4](https://user-images.githubusercontent.com/64368194/82424604-0ad06e00-9aa3-11ea-80ba-aa00350b9bb2.png)


## 4. This is use to create your own network:-

![Redhat 8  Running  - Oracle VM VirtualBox screenshot 9](https://user-images.githubusercontent.com/64368194/82424778-4a975580-9aa3-11ea-9ef6-6e5f75e1f74d.png)


## 5. This is use to create your own container using your own network:-

![Redhat 8  Running  - Oracle VM VirtualBox screenshot10](https://user-images.githubusercontent.com/64368194/82424982-89c5a680-9aa3-11ea-906e-e443f4018428.png)




# B:- Remote system:-

## 1. This is using your remote system IP address and password to login in your remote system:-


![Redhat 8  Running  - Oracle VM VirtualBox screenshot5](https://user-images.githubusercontent.com/64368194/82425139-c0032600-9aa3-11ea-99b9-13dd5a68ada0.png)


## 2. This is use to pull any image in your remote system:-

![Redhat 8  Running  - Oracle VM VirtualBox screenshot6](https://user-images.githubusercontent.com/64368194/82425410-196b5500-9aa4-11ea-9472-0f950d0f0d5f.png)



## 3. This is use to create your container in your remote system:-

## 4. This is use to create your own network in remote system:-

## 5. This is use to create your own container using your own created network in your  remote system:-    
 
 # OUTPUT:--- 3, 4 , 5 
 
  ![Redhat 8  Running  - Oracle VM VirtualBox screenshot8](https://user-images.githubusercontent.com/64368194/82425583-546d8880-9aa4-11ea-9121-c8fda9bf8188.png)
   

# TurtleBot3 

## PC Setup
- desktop에 설치된 것을 해보는 걸로
## SBC Setup
- 우빈님이 진행한 것
### [OpenCR Setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/opencr_setup/#opencr-setup)
OpenCR Setup할 때 OPENCR_PORT와 OPENCR_MODEL이 경로 설정이 제대로 되어있는지 알아야 한다. 확인하는 명령어로는 ```echo $OPENCR_PORT```또는 ```echo $OPENCR_MODEL```에 입력해야한다. 만약 파라미터 설정이 안되있으면 빈칸이 나온다.


[OpenCR Test](https://emanual.robotis.com/docs/en/platform/turtlebot3/opencr_setup/#opencr-test)에 실패할 경우 Arduino로 Dynamixel 모터를 Setup해야한다. 

### [Setup DYNAMIXELs for TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/faq/#setup-dynamixels-for-turtlebot3)  
 먼저 모터가 돌아가는 것을 확인하기 위해서는 [Arduino를 설치](https://emanual.robotis.com/docs/en/software/arduino_ide/)해야한다.  
 Arduino를 설치한 후에 board manager에 opencr를 설치해야 turtlebot3 예제를 진행할 수 있다. 

Arduino의 Serial monitor를 실행해서 Setup 을 진행한다. 
아래와 같이 화면이 나와서 모터가 돌아가면 성공한거다.  
![img](https://emanual.robotis.com/assets/images/platform/turtlebot3/faq/dynamixel_setup_6.png)


### Bringup 

1. HOST PC에서 ```roscore```를 실행한다. 
2. HOST PC에서 새로운 터미널 창을 열고 ```roslaunch turtlebot3_bringup turtlebot3_robot.launch```을 실행한다. (TURTLEBOT3_MODEL은 buger로 설정)

### Teleoperation

3. HOST PC에서 새로운 터미널 창을 열고 ```roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch```을 실행한다.(TURTLEBOT3_MODEL은 buger로 설정)



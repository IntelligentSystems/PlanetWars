# a command that works on Linux/Mac
# the arguments are passed in the same order as in the standard command

MAP=$1 
PLAYER1=$2
PLAYER2=$3
MODE=$4
NTURN=$5
MAXT=$6



java -jar tools/PlayGame.jar tools/maps/$MAP  "java $PLAYER1 " "java $PLAYER2 "    | python tools/visualizer/visualize_locally.py 2>log.txt


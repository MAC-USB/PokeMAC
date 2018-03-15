MENSAJE_READ="[Enter para continuar] "

intentos=1

function trapear {
    trap insultar SIGHUP
    trap insultar SIGINT
    trap insultar SIGQUIT
    trap insultar SIGILL
    trap insultar SIGTRAP
    trap insultar SIGABRT
    trap insultar SIGBUS
    trap insultar SIGFPE

    trap insultar SIGUSR1
    trap insultar SIGSEGV
    trap insultar SIGUSR2
    trap insultar SIGPIPE
    trap insultar SIGALRM
    trap insultar SIGTERM
    trap insultar SIGSTOP
    trap insultar SIGTSTP
    echo ""
}

function inicio {

    clear 
    echo "Hola preprador, mi PID es: $$"
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat drawings/meowth.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dialogues/dialogo_inicioPOKEMAC.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dialogues/dialogo_inicioMeowth.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    # cat dialogos/dialogo_mascaraA.txt
    # printf "\n\n\n"
    # read -p "$MENSAJE_READ"       
    # clear
    cat drawings/meowth.txt
}

function dormir {
    for i in `seq 1 100000`
    do
        p=""
    done
}

function go_evil {
    mplayer sounds/trainer.mp3 >/dev/null 2>/dev/null &  
    cat drawings/trainer.txt
    sleep 0.3
    trapear  
    while true
    do
    read -p ""
    printf "\nNo lograras derrotarme. Mejor vete a hacer admision al otro laboratorio.\n"
    done
}

function insultar {
    if [ $((intentos % 5)) = 0 -a $intentos -ne 0 ]
        then 
            printf "\nAsh tiene más posibilidades de pasar la liga que tú.\n"
        else 
            printf "\nEres más lento que un Slowpoke...\n"
    fi
    intentos=$((intentos+1))
    sleep 0.3
}

#Esto es del de zelda
function final {
    clear 
    cat dialogos/dialogo_fintemplos.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dibujos/majora.txt
    sleep 5
    while true
    do
    clear
    cat dialogos/dialogo_ponersemascara.txt
    printf "\n\n\n"
    read -p "[SI/NO para continuar] " respuesta

    if [ $respuesta = "NO" -o  $respuesta = "no" ]
    then
        clear
        cat dialogos/dialogo_ponersemascara_no.txt
        printf "\n\n\n"
        read -p "$MENSAJE_READ"       
        break
    elif [  $respuesta = "SI" -o $respuesta = "si" ]
    then
        break
    else
        clear
        echo $respuesta
        printf "\n\nNo entiendo lo que dices..."
        printf "\n\n\n"
        read -p "$MENSAJE_READ"       
    fi
    done
    clear
    printf "\n\nNavi se puso la mascara y se esta transformando!"
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    go_evil
}

function entregar_item {
    
    case $1 in 
    "42" ) #Cuando encuentra a PIKACHU
        clear
        #chmod 777 -R /home/entrenador/tunel_roca
        chmod +x scripts/pikachu.sh
        cat dialogues/dialogo_recupera_pikachu.txt
        printf "\n\n\n"
        read -p "$MENSAJE_READ"             
        clear
        cat drawings/meowth.txt
        ;;  
    "atrapado" ) #Cuando encuentra a Blastoise
        clear
        #chmod 777 -R /home/entrenador/islas_remolino
        chmod +x scripts/blastoise.sh
        cat dialogues/dialogo_recupera_blastoise.txt
        printf "\n\n\n"
        read -p "$MENSAJE_READ"       
        clear
        cat drawings/meowth.txt
        ;;  
    "nexplant" ) #Cuando recupera a Charizard
        clear
        #chmod 777 -R /home/entrenador/monte_plateado
        chmod +x scripts/charizard.sh
        cat dialogues/dialogo_recupera_charizard.txt
        printf "\n\n\n"
        read -p "$MENSAJE_READ"       
        clear
        cat drawings/meowth.txt
        ;;  
    "r3D" ) #Cuando recupera a Venusaur y va al final
        clear
        cat dialogues/dialogo_recupera_venusaur.txt
        printf "\n\n\n"
        read -p "$MENSAJE_READ"
        clear
        cat dialogues/dialogo_recupera_todos.txt
        printf "\n\n\n"
        read -p "$MENSAJE_READ"
        clear
        go_evil
        ;;
    * )
        clear
        cat drawings/meowth.txt
        echo " "
        echo "                 Meeeeeooooooooooooooowth..."
        echo " "
        echo "      ¿Qué dices? No te entiendo. Así no puedo ayudarte."
        ;;
    esac
}

#main

inicio

while true ;
do
    printf "\n[Dime una contraseña para ayudarte] "
    read -t 30 pregunta
    if [ ! -z $pregunta ]
    then
    entregar_item $pregunta
    continue
    else
    clear
    #kill -20 $$ 
    cat drawings/meowth.txt
    echo " "
    echo " "
    echo "                 Meeeeeooooooooooooooowth..."
    fi
done

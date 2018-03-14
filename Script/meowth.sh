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
    cat dibujos/toad.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dialogos/dialogo_inicio.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    cat dialogos/dialogo_inicio2.txt
    printf "\n\n\n"
    read -p "$MENSAJE_READ"
    clear
    # cat dialogos/dialogo_mascaraA.txt
    # printf "\n\n\n"
    # read -p "$MENSAJE_READ"
    # clear
    cat dibujos/toad.txt
}

function dormir {
    for i in `seq 1 100000`
    do
        p=""
    done
}

function go_evil {
    cat dibujos/bowser.txt
    sleep 0.3
    trapear
    while true
    do
	read -p ""
	printf "\nTus palabras son insignificantes. Mejor vete a hacer admisión al otro laboratorio.\n"
    done
}

function insultar {
	if [ $((intentos % 5)) = 0 -a $intentos -ne 0 ]
		then
			printf "\nNo le soples tanto al cartucho... Todos sus intentos son INUTILES\n"
		else
    		printf "\nBuen intento. Pero eso solo funciona en el N64.\n"
    fi
    intentos=$((intentos+1))
    sleep 0.3
}

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
	"1604" )
	    clear
	    chmod 777 -R /home/Mario/Castillo_de_KingBoo
	    cat dialogos/dialogo_mascaraE.txt
	    printf "\n\n\n"
	    read -p "$MENSAJE_READ"
	    clear
	    cat dibujos/toad.txt
	    ;;
	"superstar" )
	    clear
	    chmod 777 -R /home/Mario/Castillo_de_Bowser_jr
	    cat dialogos/dialogo_mascaraF.txt
	    printf "\n\n\n"
	    read -p "$MENSAJE_READ"
	    clear
	    cat dibujos/toad.txt
	    ;;
	"plant" )
	    clear
	    chmod 777 -R /home/Mario/Castillo_de_Pirana_plant
	    cat dialogos/dialogo_mascaraET.txt
	    printf "\n\n\n"
	    read -p "$MENSAJE_READ"
	    clear
	    cat dibujos/toad.txt
	    ;;
	"b0ws3r" )
	    clear
	    go_evil
	    ;;
	* )
	    echo "Lo siento, no te entiendo. Esa frase no corresponde a ninguna mascara"
	    ;;
    esac
}

inicio

while true ;
do
    printf "\n[Dime una contraseña para entregarte un item] "
    read -t 30 pregunta
    if [ ! -z $pregunta ]
	then
	entregar_item $pregunta
	continue
    else
	clear
	printf "\n\n\n Whhhhuuuuuuusssshhhh..."
	kill -20 $$
	cat dibujos/toad.txt
    fi
done

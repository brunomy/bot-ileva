java_pids=$(ps aux | grep java | grep -v grep | awk '{print $2}')
for pid in $java_pids; do
    echo "Finalizando processo Java com PID: $pid"
    kill -9 $pid
done

echo "Compilação concluída e processos Java finalizados."
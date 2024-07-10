from datetime import datetime, timedelta


def convert_time(hora: str) -> datetime:
    try:
        return datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=int(hora.split(":")[0]),
            minute=int(hora.split(":")[1])
        )
    except ValueError:
        return datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=0,
            minute=0
        )


deu_entrada: datetime = convert_time(input("Que horas deu entrada? "))
saiu_para_almoco: datetime = convert_time(input("Que horas saiu para almoço? "))
voltou_do_almoco: datetime = convert_time(input("Que horas voltou do almoço? "))

print(f"\n{deu_entrada.strftime("%H:%M")} → a hora que bateu ponto de entrada.")
print(f"{(deu_entrada + timedelta(hours=6, minutes=15)).strftime('%H:%M')} → a hora da saída normal (15 minutos).")

if saiu_para_almoco.strftime("%H:%M") != "00:00" and voltou_do_almoco.strftime("%H:%M") != "00:00":
    duration = voltou_do_almoco - saiu_para_almoco
    print(f"{duration.seconds / 60:.0f} minutos foi o tempo de duração de almoço.")
    print(f"{(deu_entrada + timedelta(hours=6) + duration).strftime('%H:%M')} → a hora da saída sem hora extra.")
    print(f"{(deu_entrada + timedelta(hours=7) + duration).strftime('%H:%M')} → a hora da saída com 1 hora extra.")
    print(f"{(deu_entrada + timedelta(hours=8) + duration).strftime('%H:%M')} → a hora da saída com 2 horas extra.")
else:
    print("Não deu ponto de entrada e saída do almoço...")

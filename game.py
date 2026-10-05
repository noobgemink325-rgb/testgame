import random
import time

def game_rpg():
    player_hp = 100
    monster_hp = 80
    monster_name = "Naga Mini"

    print("=== GAME RPG PETUALANGAN TERMINAL ===")
    print(f"Seekor {monster_name} muncul di hadapanmu!\n")

    while player_hp > 0 and monster_hp > 0:
        print(f"HP Kamu: {player_hp} | HP {monster_name}: {monster_hp}")
        print("Pilih aksi:")
        print("1. Serang")
        print("2. Minum Ramuan (Heal)")
        print("3. Lari")
        
        pilihan = input("Masukkan pilihan (1/2/3): ")
        print("-" * 30)

        if pilihan == "1":
            damage = random.randint(15, 30)
            monster_hp -= damage
            print(f"Kamu menebas {monster_name} dan memberikan {damage} damage!")
        elif pilihan == "2":
            heal = random.randint(10, 25)
            player_hp += heal
            print(f"Kamu minum ramuan dan memulihkan {heal} HP!")
        elif pilihan == "3":
            if random.choice([True, False]):
                print("Kamu berhasil kabur dengan selamat! Game selesai.")
                return
            else:
                print("Gagal kabur! Monster menahan langkahmu.")
        else:
            print("Pilihan gak valid, kamu kehilangan giliran!")

        # Giliran Monster Menyerang
        if monster_hp > 0:
            time.sleep(1)
            monster_damage = random.randint(10, 25)
            player_hp -= monster_damage
            print(f"{monster_name} menyerang balik dan memberikan {monster_damage} damage!\n")
        
        time.sleep(1)

    # Hasil Akhir
    if player_hp > 0:
        print(f"Selamat! Kamu berhasil mengalahkan {monster_name}!")
    else:
        print("HP kamu habis... Game Over!")

if __name__ == "__main__":
    game_rpg()

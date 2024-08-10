#pgzero

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Uzaylı Yarışı" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı

# Nesneler
uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("arkaplan")
kutu = Actor('kutu', (550, 265))
new_image = 'uzaylı' # Anlık Görüntüyü Takip Eder
ari = Actor('arı', (850, 175))
ob = Actor("OB")

oyun_sonu = 0
puan = 0

def draw():
    if oyun_sonu == 0:
        arkaplan.draw()
        uzayli.draw()
        kutu.draw()
        ari.draw()
        screen.draw.text(puan, pos=(10, 10), color="white", fontsize = 24)
    else:
        ob.draw()
        screen.draw.text("Enter'e Basınız", center=(300, 83), color="red", fontsize = 40)
        
def update(dt):
    global new_image
    global oyun_sonu
    global puan
    # Arının Hareketi
    if ari.x > -20:
        ari.x = ari.x - 5
    else:
        puan += 1
        ari.x = WIDTH + 20
    
    if oyun_sonu == 1:
        if keyboard.enter:  
            uzayli.pos = (50, 240)
            kutu.pos = (550, 265)
            ari.pos = (850, 175)
            oyun_sonu = 0
            puan = 0
            
            
    # Kutunun Hareketi
    if kutu.x > -20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else:
        kutu.x = WIDTH + 20
        puan += 1
        
    # Kontroller
    if keyboard.left or keyboard.a and uzayli.x > 20:
        uzayli.x = uzayli.x - 5
        if new_image != 'sol':
            uzayli.image = 'sol'
            new_image = 'sol'
    elif keyboard.right or keyboard.d and uzayli.x < 580:
        uzayli.x = uzayli.x + 5
        if new_image != 'sağ':
            uzayli.image = 'sağ'
            new_image = 'sağ'
    elif keyboard.down or keyboard.s:
        if new_image != 'eğilme':
            uzayli.image = 'eğilme'
            new_image = 'eğilme'
            uzayli.y = 250
    else:
        if uzayli.y > 240 and new_image == 'eğilme':
            uzayli.image = 'uzaylı'
            new_image = 'uzaylı'
            uzayli.y = 240
    
    # Çarpışma 
    if uzayli.colliderect(kutu):
        oyun_sonu = 1
        # if new_image != 'yaralı':
        #     uzayli.image = 'yaralı'
        #     new_image = 'yaralı'
            
    if uzayli.colliderect(ari):
        oyun_sonu = 1
        # if new_image != 'yaralı':
        #     uzayli.image = 'yaralı'
        #     new_image = 'yaralı'
        
def on_key_down(key):
    # Zıplama
    if keyboard.space or keyboard.up or keyboard.w:
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)
        
        

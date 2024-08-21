#pgzero

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Uzaylı Yarışı" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı

# Nesneler
uzayli= Actor('uzaylı', (50, 240))
arkaplan = Actor("arkaplan")
kutu = Actor('kutu', (550, 265))
new_image = 'uzaylı' # Mevcut Resmi Takip Eder
ari = Actor('arı', (850, 170))

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
    ari.draw()
    
def update(dt):
    global new_image
    # Kutunun Hareketi
    if kutu.x > -20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else:
        kutu.x = WIDTH + 20
        
    # Arinin Hareketi
    if ari.x > -20:
        ari.x = ari.x - 5
    else:
        ari.x = WIDTH + 20
        
    # Kontroller
    if keyboard.left or keyboard.a and uzayli.x > 20:
        uzayli.x =uzayli.x - 5
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
            
    if uzayli.colliderect(kutu): # Karakter kutuyla çarpışırsa
        uzayli.image = 'yaralı'
        
    else:
        uzayli.image = 'uzaylı'
        
def on_key_down(key):
    # Zıplama
    if keyboard.space or keyboard.up or keyboard.w:
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)
        
        

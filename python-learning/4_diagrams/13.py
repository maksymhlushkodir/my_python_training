import matplotlib.pyplot as plt

musics = ['Winds Of Powhatan', 'Fatui Harbinger`s Theme', 'Harbinger`s Omen', 'Port Ormos Theme',
          'Raiden Shogun`s Theme', 'All is Found - Cover', 'Froze Heat - Cover']
estimates = [80, 97, 100, 100, 85, 101, 115]

plt.bar(musics, estimates, color='yellow')
plt.title('good musics\n Frostudio Chambersonic')
plt.ylabel('points')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
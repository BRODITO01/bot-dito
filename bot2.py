import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def minimal(ctx):
    await ctx.send(f'Hi! I am a {bot.user} , minimal hari sabtu minggu libur bos anjay!')


@bot.command()
async def apa_saja_contoh_bahan_sekali_pakai(ctx):
    await ctx.send('''Apa Saja Yang Termasuk dalam Barang Habis Pakai?

1. Kemasan Kemasan adalah salah satu barang habis pakai yang paling sering kita temui. 
2. Makanan dan Minuman Makanan dan minuman adalah barang habis pakai yang paling umum. 
3. Tisu dan Sapu Tangan Tisu dan sapu tangan adalah barang habis pakai yang sering kita gunakan dalam kehidupan sehari-hari 
4.DSB''')

@bot.command()
async def contoh_bahan_daur_ulang(ctx):
    await ctx.send('''contoh bahan daur ulang dan cara pembuatannya                                                                                                                                                  Toples Permen
Kerajinan dari botol bekas yang pertama adalah toples permen. Untuk membuatnya, siapkan sejumlah alat yakni gunting, kuas, cat acrylic, lem dan karton. Bila semua sudah siap, ikuti langkah-langkah berikut:

- Siapkan satu botol plastik lalu dipotong menjadi dua bagian
- Bagian atas dari botol digunting dan ditekuk ke bawah hingga membentuk bunga
- Seluruh permukaan botol dicat dengan cat acrylic
- Kini saatnya membuat tutup toples, langkah pertama gunting karton yang ukurannya sama dengan besar diameter toples dan lapisi dengan kain perca
- Setelah itu, rapikan bagian tepinya ke bagian dalam. Setelah itu gabungkan keduanya hingga berbentuk tutup toples
- Tambahkan dengan berbagai hiasan
- Selesai, kini toples permen telah jadi dibentuk''')

@bot.command()
async def cara_mengurangi_sampah(ctx):
    await ctx.send('''1.kurangi penggunaan kantong dan botol plastik sekali pakai 
2. Gunakan piring, mangkuk berbahan kaca dan yang bukan sekali pakai 
3. kurangi belanja bahan yang hanya sekali pakai 
4. Daur ulang barang yang sudah tidak bisa dipakai''')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('Slide2.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

bot.run("MTE1NTA2Mzk1NzUyNzIwNzk3Ng.GdWMdS.eBbNu6J1eKqI2BI2-ktR9RpbRiCJWm23lVROm8")

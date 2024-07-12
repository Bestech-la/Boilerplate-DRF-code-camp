# Generated by Django 5.0.7 on 2024-07-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(choices=[('ນະຄອນຫຼວງວຽງຈັນ', 'Vientiane Prefecture'), ('ແຂວງຜົ້ງສາລີ', 'Phongsaly'), ('ແຂວງຫຼວງນໍ້າທາ', 'Luang Namtha'), ('ແຂວງອຸດົມໄຊ', 'Oudomxay'), ('ແຂວງບໍ່ແກ້ວ', 'Bokeo'), ('ແຂວງຫຼວງພະບາງ', 'Luangprabang'), ('ແຂວງຫົວພັນ', 'Houaphanh'), ('ແຂວງໄຊຍະບູລີ', 'Sainyabuli'), ('ແຂວງຊຽງຂວາງ', 'Xiangkhouang'), ('ແຂວງວຽງຈັນ', 'Vientiane Province'), ('ແຂວງບໍລິຄຳໄຊ', 'Bolikhamsai'), ('ແຂວງຄຳມ່ວນ', 'Khammouane'), ('ແຂວງສະຫວັນນະເຂດ', 'Savannakhet'), ('ແຂວງສາລະວັນ', 'Salavan'), ('ແຂວງເຊກອງ', 'Sekong'), ('ແຂວງຈຳປາສັກ', 'Champasak'), ('ແຂວງອັດຕະປື', 'Attapue'), ('ແຂວງໄຊສົມບູນ', 'Xaisomboun')], max_length=35)),
                ('district_name', models.CharField(choices=[('ເມືອງຈັນທະບູລີ', 'Chanthabuly'), ('ເມືອງສີໂຄດຕະບອງ', 'Sikhottabong'), ('ເມືອງໄຊເສດຖາ', 'Xaysetha'), ('ເມືອງສີສັດຕະນາກ', 'Sisattanak'), ('ເມືອງນາຊາຍທອງ', 'Naxaithong'), ('ເມືອງໄຊທານີ', 'Xaythany'), ('ເມືອງຫາດຊາຍຟອງ', 'Hadxayfong'), ('ເມືອງສັງທອງ', 'Sangthong'), ('ເມືອງປາກງື່ມ', 'Mayparkngum'), ('ເມືອງຜົ້ງສາລີ', 'Phongsaly'), ('ເມືອງໃໝ່', 'May'), ('ເມືອງຂວາ', 'Khoua'), ('ເມືອງສຳພັນ', 'Sampanh'), ('ເມືອງບຸນເໜືອ', 'Boun Neua'), ('ເມືອງຍອດອູ', 'Yotou'), ('ເມືອງບຸນໃຕ້', 'Boun Tay'), ('ເມືອງຫຼວງນໍ້າທາ', 'Namtha'), ('ເມືອງສີງ', 'Sing'), ('ເມືອງລອງ', 'Long'), ('ເມືອງວຽງພູຄາ', 'Viengphoukha'), ('ເມືອງນາແລ', 'Nale'), ('ເມືອງໄຊ', 'Xay'), ('ເມືອງຫຼາ', 'La'), ('ເມືອງນາໝໍ້', 'Namo'), ('ເມືອງງາ', 'Nga'), ('ເມືອງແບ່ງ', 'Beng'), ('ເມືອງຮຸນ', 'Houne'), ('ເມືອງປາກແບ່ງ', 'Pakbeng'), ('ເມືອງຫ້ວຍຊາຍ', 'Houayxay'), ('ເມືອງຕົ້ນເຜິ້ງ', 'Tonpheung'), ('ເມືອງເມິງ', 'Meung'), ('ເມືອງຜາອຸດົມ', 'Phaoudom'), ('ເມືອງປາກທາ', 'Paktha'), ('ເມືອງຫຼວງພະບາງ', 'Luangprabang'), ('ເມືອງຊຽງເງິນ', 'Xiengeneun'), ('ເມືອງນານ', 'Nane'), ('ເມືອງປາກອູ', 'Pakou'), ('ເມືອງນ້ຳບາກ', 'Nambak'), ('ເມືອງງອຍ', 'Ngoy'), ('ເມືອງປາກແຊງ', 'Pakseng'), ('ເມືອງໂພນໄຊ', 'Phonxay'), ('ເມືອງຈອມເພັດ', 'Chomphet'), ('ເມືອງວຽງຄຳ', 'Viengkhamluangprabang'), ('ເມືອງພູຄູນ', 'Phoukhoune'), ('ເມືອງໂພນທອງ', 'Phonthongluangprabang'), ('ເມືອງຊຽງເງີນ', 'Xiangngeun'), ('ເມືອງຊຳເໜືອ', 'Xamneua'), ('ເມືອງຊຽງຄໍ້', 'Xiengkho'), ('ເມືອງວຽງທອງ', 'Viengthonghouaphanh'), ('ເມືອງວຽງໄຊ', 'Viengxay'), ('ເມືອງຫົວເມືອງ', 'Houameuang'), ('ເມືອງຊຳໃຕ້', 'Samtay'), ('ເມືອງສົບເບົາ', 'Sopbao'), ('ເມືອງແອດ', 'Et'), ('ເມືອງກອັນ', 'Kone'), ('ເມືອງຊ່ອນ', 'Xon'), ('ເມືອງໄຊຍະບູລີ', 'Sainyabuli'), ('ເມືອງຄອບ', 'Khop'), ('ເມືອງຫົງສາ', 'Hongsa'), ('ເມືອງເງິນ', 'Ngeun'), ('ເມືອງຊຽງຮ່ອນ', 'Xienghone'), ('ເມືອງພຽງ', 'Phiang'), ('ເມືອງປາກລາຍ', 'Parklai'), ('ເມືອງແກ່ນທ້າວ', 'Kenethao'), ('ເມືອງບໍ່ແຕນ', 'Botene'), ('ເມືອງທົ່ງມີໄຊ', 'Thongmyxay'), ('ເມືອງໄຊສະຖານ', 'Xaisathan'), ('ເມືອງແປກ', 'Pek'), ('ເມືອງຄຳ', 'Kham'), ('ເມືອງໜອງແຮດ', 'Nonghet'), ('ເມືອງຄູນ', 'Khoune'), ('ເມືອງໝອກໃໝ່', 'Mokmay'), ('ເມືອງພູກູດ', 'Phoukout'), ('ເມືອງຜາໄຊ', 'Phaxay'), ('ເມືອງໂພນໂຮງ', 'Phonhong'), ('ເມືອງທຸລະຄົມ', 'Thoulakhom'), ('ເມືອງແກ້ວອຸດົມ', 'Keooudom'), ('ເມືອງກາສີ', 'Kasy'), ('ເມືອງວັງວຽງ', 'Vangvieng'), ('ເມືອງເຟືອງ', 'Feuang'), ('ເມືອງຊະນະຄາມ', 'Xanakharm'), ('ເມືອງແມດ', 'Mad'), ('ເມືອງວຽງຄໍາ', 'Viengkham Xiangkhouang'), ('ເມືອງຫີນເຫີບ', 'Hinhurp'), ('ເມືອງໝື່ນ', 'Meun'), ('ເມືອງປາກຊັນ', 'Pakxan'), ('ເມືອງທ່າພະບາດ', 'Thaphabat'), ('ເມືອງປາກກະດິງ', 'Pakkading'), ('ເມືອງບໍລິຄັນ', 'Borikhane'), ('ເມືອງຄຳເກີດ', 'Khamkeut'), ('ເມືອງໄຊຈຳພອນ', 'Xaichamphon'), ('ເມືອງທ່າແຂກ', 'Thakhek'), ('ເມືອງມະຫາໄຊ', 'Mahaxay'), ('ເມືອງໜອງບົກ', 'Nong Bok'), ('ເມືອງຫີນບູນ', 'Hineboune'), ('ເມືອງຍົມມະລາດ', 'Yommalath'), ('ເມືອງບົວລະພາ', 'Boualapha'), ('ມືອງນາກາຍ', 'Nakai'), ('ເມືອງເຊບັ້ງໄຟ', 'Sebangphay'), ('ເມືອງໄຊບົວທອງ', 'Xaibouathong'), ('ເມືອງຄູນຄຳ', 'Kounkham'), ('ເມືອງໄກສອນ ພົມວິຫານ', 'Kaysone Phomvihane'), ('ເມືອງອຸທຸມພອນ', 'Outhoumphone'), ('ເມືອງອາດສະພັງທອງ', 'Atsaphangthong'), ('ເມືອງພີນ', 'Phine'), ('ເມືອງເຊໂປນ', 'Seponh'), ('ເມືອງນອງ', 'Nong'), ('ເມືອງທ່າປາງທອງ', 'Thapangthong'), ('ເມືອງສອງຄອນ', 'Songkhone'), ('ເມືອງຈຳພອນ', 'Champhone'), ('ເມືອງຊົນນະບູລີ', 'Xonaboury'), ('ເມືອງໄຊບູລີ', 'Xayboury'), ('ເມືອງວີລະບຸລີ', 'Viraboury'), ('ເມືອງອາດສະພອນ', 'Assaphone'), ('ເມືອງໄຊພູທອງ', 'Xonboury'), ('ເມືອງພະລານໄຊ', 'Thaphalanxay'), ('ເມືອງສາລະວັນ', 'Saravane'), ('ເມືອງຕະໂອ້ຍ', 'Taoy'), ('ເມືອງຕຸ້ມລານ', 'Toumlane'), ('ເມືອງລະຄອນເພັງ', 'Lakhonepheng'), ('ເມືອງວາປີ', 'Vapy'), ('ເມືອງຄົງເຊໂດນ', 'Khongsedone'), ('ເມືອງເລົ່າງາມ', 'Laongam'), ('ເມືອງສະມ້ວຍ', 'Samouay'), ('ເມືອງລະມາມ', 'Lamam'), ('ເມືອງກະເລິມ', 'Kaleum'), ('ເມືອງດາກຈຶງ', 'Dakcheung'), ('ເມືອງທ່າແຕງ', 'Thateng'), ('ເມືອງປາກເຊ', 'Pakse'), ('ເມືອງຊະນະສົມບູນ', 'Sanasomboun'), ('ເມືອງບາຈຽງຈະເລີນສຸກ', 'Batiengchaleungsouk'), ('ເມືອງປາກຊ່ອງ', 'Paksong'), ('ເມືອງປະທຸມພອນ', 'Pathouphone'), ('ເມືອງຈຳປາສັກ', 'Champassack'), ('ເມືອງສຸຂຸມາ', 'Soukhoumma'), ('ເມືອງມູນລະປະໂມກ', 'Mounlapamok'), ('ເມືອງໂຂງ', 'Khong'), ('ເມືອງໄຊເຊດຖາ', 'Saysetha'), ('ເມືອງສາມັກຄີໄຊ', 'Samakkhixay'), ('ເມືອງສະໜາມໄຊ', 'Sanamxay'), ('ເມືອງຊານໄຊ', 'Sanxay'), ('ເມືອງພູວົງ', 'Phouvong'), ('ເມືອງອະນຸວົງ', 'Anouvong'), ('ເມືອງລ້ອງແຈ້ງ', 'Longchaeng'), ('ເມືອງລ້ອງຊານ', 'Longxan'), ('ເມືອງເມືອງຮົ່ມ', 'Hom'), ('ເມືອງທ່າໂທມ', 'Thathom')], max_length=35)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'District Info',
                'ordering': ['-created_on'],
            },
        ),
    ]

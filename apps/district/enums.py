from enum import Enum

class ProvinceChoices(Enum):
    VIENTIANE_PREFECTURE = "ນະຄອນຫຼວງວຽງຈັນ"
    PHONGSALY = "ແຂວງຜົ້ງສາລີ"
    LUANG_NAMTHA = "ແຂວງຫຼວງນໍ້າທາ"
    OUDOMXAY = "ແຂວງອຸດົມໄຊ"
    BOKEO = "ແຂວງບໍ່ແກ້ວ"
    LUANGPRABANG = "ແຂວງຫຼວງພະບາງ"
    HOUAPHANH = "ແຂວງຫົວພັນ"
    SAINYABULI = "ແຂວງໄຊຍະບູລີ"
    XIANGKHOUANG = "ແຂວງຊຽງຂວາງ"
    VIENTIANE_PROVINCE = "ແຂວງວຽງຈັນ"
    BOLIKHAMSAI = "ແຂວງບໍລິຄຳໄຊ"
    KHAMMOUANE = "ແຂວງຄຳມ່ວນ"
    SAVANNAKHET = "ແຂວງສະຫວັນນະເຂດ"
    SALAVAN = "ແຂວງສາລະວັນ"
    SEKONG = "ແຂວງເຊກອງ"
    CHAMPASAK = "ແຂວງຈຳປາສັກ"
    ATTAPUE = "ແຂວງອັດຕະປື"
    XAISOMBOUN = "ແຂວງໄຊສົມບູນ"

    @classmethod
    def choices(cls):
        """Return choices as a list of tuples."""
        return [(choice.value, choice.name.replace("_", " ").title()) for choice in cls]

class DistrictChoices(Enum):
    # Vientiane Prefecture
    CHANTHABULY = "ເມືອງຈັນທະບູລີ"
    SIKHOTTABONG = "ເມືອງສີໂຄດຕະບອງ"
    XAYSETHA = "ເມືອງໄຊເສດຖາ"
    SISATTANAK = "ເມືອງສີສັດຕະນາກ"
    NAXAITHONG = "ເມືອງນາຊາຍທອງ"
    XAYTHANY = "ເມືອງໄຊທານີ"
    HADXAYFONG = "ເມືອງຫາດຊາຍຟອງ"
    SANGTHONG = "ເມືອງສັງທອງ"
    MAYPARKNGUM = "ເມືອງປາກງື່ມ"

    # Phongsaly Province
    PHONGSALY = "ເມືອງຜົ້ງສາລີ"
    MAY = "ເມືອງໃໝ່"
    KHOUA = "ເມືອງຂວາ"
    SAMPANH = "ເມືອງສຳພັນ"
    BOUN_NEUA = "ເມືອງບຸນເໜືອ"
    YOTOU = "ເມືອງຍອດອູ"
    BOUN_TAY = "ເມືອງບຸນໃຕ້"

    # Luang Namtha Province
    NAMTHA = "ເມືອງຫຼວງນໍ້າທາ"
    SING = "ເມືອງສີງ"
    LONG = "ເມືອງລອງ"
    VIENGPHOUKHA = "ເມືອງວຽງພູຄາ"
    NALE = "ເມືອງນາແລ"

    # Oudomxay Province
    XAY = "ເມືອງໄຊ"
    LA = "ເມືອງຫຼາ"
    NAMO = "ເມືອງນາໝໍ້"
    NGA = "ເມືອງງາ"
    BENG = "ເມືອງແບ່ງ"
    HOUNE = "ເມືອງຮຸນ"
    PAKBENG = "ເມືອງປາກແບ່ງ"

    # Bokeo Province
    HOUAYXAY = "ເມືອງຫ້ວຍຊາຍ"
    TONPHEUNG = "ເມືອງຕົ້ນເຜິ້ງ"
    MEUNG = "ເມືອງເມິງ"
    PHAOUDOM = "ເມືອງຜາອຸດົມ"
    PAKTHA = "ເມືອງປາກທາ"

    # Luang Prabang Province
    LUANGPRABANG = "ເມືອງຫຼວງພະບາງ"
    XIENGENEUN = "ເມືອງຊຽງເງິນ"
    NANE = "ເມືອງນານ"
    PAKOU = "ເມືອງປາກອູ"
    NAMBAK = "ເມືອງນ້ຳບາກ"
    NGOY = "ເມືອງງອຍ"
    PAKSENG = "ເມືອງປາກແຊງ"
    PHONXAY = "ເມືອງໂພນໄຊ"
    CHOMPHET = "ເມືອງຈອມເພັດ"
    VIENGKHAMLUANGPRABANG = "ເມືອງວຽງຄຳ"
    PHOUKHOUNE = "ເມືອງພູຄູນ"
    PHONTHONGLUANGPRABANG = "ເມືອງໂພນທອງ"
    XIANGNGEUN = "ເມືອງຊຽງເງີນ"


    # Houaphanh Province
    XAMNEUA = "ເມືອງຊຳເໜືອ"
    XIENGKHO = "ເມືອງຊຽງຄໍ້"
    VIENGTHONGHOUAPHANH = "ເມືອງວຽງທອງ"
    VIENGXAY = "ເມືອງວຽງໄຊ"
    HOUAMEUANG = "ເມືອງຫົວເມືອງ"
    SAMTAY = "ເມືອງຊຳໃຕ້"
    SOPBAO = "ເມືອງສົບເບົາ"
    ET = "ເມືອງແອດ"
    KONE = "ເມືອງກອັນ"
    XON = "ເມືອງຊ່ອນ"

    # Sainyabuli Province
    SAINYABULI = "ເມືອງໄຊຍະບູລີ"
    KHOP = "ເມືອງຄອບ"
    HONGSA = "ເມືອງຫົງສາ"
    NGEUN = "ເມືອງເງິນ"
    XIENGHONE = "ເມືອງຊຽງຮ່ອນ"
    PHIANG = "ເມືອງພຽງ"
    PARKLAI = "ເມືອງປາກລາຍ"
    KENETHAO = "ເມືອງແກ່ນທ້າວ"
    BOTENE = "ເມືອງບໍ່ແຕນ"
    THONGMYXAY = "ເມືອງທົ່ງມີໄຊ"
    XAISATHAN = "ເມືອງໄຊສະຖານ"

    # Xiangkhouang Province
    PEK = "ເມືອງແປກ"
    KHAM = "ເມືອງຄຳ"
    NONGHET = "ເມືອງໜອງແຮດ"
    KHOUNE = "ເມືອງຄູນ"
    MOKMAY = "ເມືອງໝອກໃໝ່"
    PHOUKOUT = "ເມືອງພູກູດ"
    PHAXAY = "ເມືອງຜາໄຊ"

    # Xiangkhouang Province
    PHONHONG = "ເມືອງໂພນໂຮງ"
    THOULAKHOM = "ເມືອງທຸລະຄົມ"
    KEOOUDOM = "ເມືອງແກ້ວອຸດົມ"
    KASY = "ເມືອງກາສີ"
    VANGVIENG = "ເມືອງວັງວຽງ"
    FEUANG = "ເມືອງເຟືອງ"
    XANAKHARM = "ເມືອງຊະນະຄາມ"
    MAD = "ເມືອງແມດ"

    VIENGKHAM_XIANGKHOUANG = "ເມືອງວຽງຄໍາ"
    HINHURP = "ເມືອງຫີນເຫີບ"
    MEUN = "ເມືອງໝື່ນ"
    
    # Bolikhamsai Province
    PAKXAN = "ເມືອງປາກຊັນ"
    THAPHABAT = "ເມືອງທ່າພະບາດ"
    PAKKADING = "ເມືອງປາກກະດິງ"
    BORIKHANE = "ເມືອງບໍລິຄັນ"
    KHAMKEUT = "ເມືອງຄຳເກີດ"
    VIENGTHONG_XIANGKHOUANG = "ເມືອງວຽງທອງ"
    XAICHAMPHON = "ເມືອງໄຊຈຳພອນ"

    # Khammouane Province
    THAKHEK = "ເມືອງທ່າແຂກ"
    MAHAXAY = "ເມືອງມະຫາໄຊ"
    NONG_BOK = "ເມືອງໜອງບົກ"
    HINEBOUNE = "ເມືອງຫີນບູນ"
    YOMMALATH = "ເມືອງຍົມມະລາດ"
    BOUALAPHA = "ເມືອງບົວລະພາ"
    NAKAI = "ມືອງນາກາຍ"
    SEBANGPHAY = "ເມືອງເຊບັ້ງໄຟ"
    XAIBOUATHONG = "ເມືອງໄຊບົວທອງ"
    KOUNKHAM = "ເມືອງຄູນຄຳ"

    # Savannakhet Province
    KAYSONE_PHOMVIHANE = "ເມືອງໄກສອນ ພົມວິຫານ"
    OUTHOUMPHONE = "ເມືອງອຸທຸມພອນ"
    ATSAPHANGTHONG = "ເມືອງອາດສະພັງທອງ"
    PHINE = "ເມືອງພີນ"
    SEPONH = "ເມືອງເຊໂປນ"
    NONG = "ເມືອງນອງ"
    THAPANGTHONG = "ເມືອງທ່າປາງທອງ"
    SONGKHONE = "ເມືອງສອງຄອນ"
    CHAMPHONE = "ເມືອງຈຳພອນ"
    XONABOURY = "ເມືອງຊົນນະບູລີ"
    XAYBOURY = "ເມືອງໄຊບູລີ"
    VIRABOURY = "ເມືອງວີລະບຸລີ"
    ASSAPHONE = "ເມືອງອາດສະພອນ"
    XONBOURY = "ເມືອງໄຊພູທອງ"
    THAPHALANXAY = "ເມືອງພະລານໄຊ"


    # Salavan Province
    SARAVANE = "ເມືອງສາລະວັນ"
    TAOY = "ເມືອງຕະໂອ້ຍ"
    TOUMLANE = "ເມືອງຕຸ້ມລານ"
    LAKHONEPHENG = "ເມືອງລະຄອນເພັງ"
    VAPY = "ເມືອງວາປີ"
    KHONGSEDONE = "ເມືອງຄົງເຊໂດນ"
    LAONGAM = "ເມືອງເລົ່າງາມ"
    SAMOUAY = "ເມືອງສະມ້ວຍ"

    # Sekong Province
    LAMAM = "ເມືອງລະມາມ"
    KALEUM = "ເມືອງກະເລິມ"
    DAKCHEUNG = "ເມືອງດາກຈຶງ"
    THATENG = "ເມືອງທ່າແຕງ"

    # Champasak Province
    PAKSE = "ເມືອງປາກເຊ"
    SANASOMBOUN = "ເມືອງຊະນະສົມບູນ"
    BATIENGCHALEUNGSOUK = "ເມືອງບາຈຽງຈະເລີນສຸກ"
    PAKSONG = "ເມືອງປາກຊ່ອງ"
    PATHOUPHONE = "ເມືອງປະທຸມພອນ"
    PHONTHONGCHAMPASAK = "ເມືອງໂພນທອງ"
    CHAMPASSACK = "ເມືອງຈຳປາສັກ"
    SOUKHOUMMA = "ເມືອງສຸຂຸມາ"
    MOUNLAPAMOK = "ເມືອງມູນລະປະໂມກ"
    KHONG = "ເມືອງໂຂງ"

    # Attapeu Province
    SAYSETHA = "ເມືອງໄຊເຊດຖາ"
    SAMAKKHIXAY = "ເມືອງສາມັກຄີໄຊ"
    SANAMXAY = "ເມືອງສະໜາມໄຊ"
    SANXAY = "ເມືອງຊານໄຊ"
    PHOUVONG = "ເມືອງພູວົງ"

    # Xaisomboun Province
    ANOUVONG = "ເມືອງອະນຸວົງ"
    LONGCHAENG = "ເມືອງລ້ອງແຈ້ງ"
    LONGXAN = "ເມືອງລ້ອງຊານ"
    HOM = "ເມືອງເມືອງຮົ່ມ"
    THATHOM = "ເມືອງທ່າໂທມ"
    
    @classmethod
    def choices(cls):
        """Return choices as a list of tuples."""
        return [(choice.value, choice.name.replace("_", " ").title()) for choice in cls]


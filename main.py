import time
from tqdm import tqdm
from time import gmtime, strftime

# Import the ADS1x15 module.
import Adafruit_ADS1x15

#Import Peewee Database ORM
from peewee import *

###############################################################################
# Database creation and definition
#
#
database = SqliteDatabase("ecudata.db")                                         # Creates ecu_data.db file if non present and stores in local folder and assigns it to database variable name

pin_list = ['pin_%s' % s for s in range(1,157)]                                 # Create a list of Pin_# for the table fields, starts one step forward (1) and ends at 157 to get 156 because range starts at 0
fields_model = {'db_ref': IntegerField(), 'ecu_ref': IntegerField(),
                'test_date': DateField(), 'is_faulty': BooleanField()}          # Create another dict with the rest of the fields
fields_pin_list = {pin_n: IntegerField() for pin_n in pin_list}                 # Iterate through all pin fields and create a dict
fields_model.update(fields_pin_list)                                            # Combine both dictionaries

# Define and create ecu_data table with the fields above from dictionary
#ecu_data = type('ecu_data', (Model,), fields_model)

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Ecu_data(BaseModel):
    db_ref = IntegerField()
    ecu_ref = IntegerField()
    is_faulty = IntegerField()
    pin_1 = IntegerField()
    pin_10 = IntegerField()
    pin_100 = IntegerField()
    pin_101 = IntegerField()
    pin_102 = IntegerField()
    pin_103 = IntegerField()
    pin_104 = IntegerField()
    pin_105 = IntegerField()
    pin_106 = IntegerField()
    pin_107 = IntegerField()
    pin_108 = IntegerField()
    pin_109 = IntegerField()
    pin_11 = IntegerField()
    pin_110 = IntegerField()
    pin_111 = IntegerField()
    pin_112 = IntegerField()
    pin_113 = IntegerField()
    pin_114 = IntegerField()
    pin_115 = IntegerField()
    pin_116 = IntegerField()
    pin_117 = IntegerField()
    pin_118 = IntegerField()
    pin_119 = IntegerField()
    pin_12 = IntegerField()
    pin_120 = IntegerField()
    pin_121 = IntegerField()
    pin_122 = IntegerField()
    pin_123 = IntegerField()
    pin_124 = IntegerField()
    pin_125 = IntegerField()
    pin_126 = IntegerField()
    pin_127 = IntegerField()
    pin_128 = IntegerField()
    pin_129 = IntegerField()
    pin_13 = IntegerField()
    pin_130 = IntegerField()
    pin_131 = IntegerField()
    pin_132 = IntegerField()
    pin_133 = IntegerField()
    pin_134 = IntegerField()
    pin_135 = IntegerField()
    pin_136 = IntegerField()
    pin_137 = IntegerField()
    pin_138 = IntegerField()
    pin_139 = IntegerField()
    pin_14 = IntegerField()
    pin_140 = IntegerField()
    pin_141 = IntegerField()
    pin_142 = IntegerField()
    pin_143 = IntegerField()
    pin_144 = IntegerField()
    pin_145 = IntegerField()
    pin_146 = IntegerField()
    pin_147 = IntegerField()
    pin_148 = IntegerField()
    pin_149 = IntegerField()
    pin_15 = IntegerField()
    pin_150 = IntegerField()
    pin_151 = IntegerField()
    pin_152 = IntegerField()
    pin_153 = IntegerField()
    pin_154 = IntegerField()
    pin_155 = IntegerField()
    pin_156 = IntegerField()
    pin_16 = IntegerField()
    pin_17 = IntegerField()
    pin_18 = IntegerField()
    pin_19 = IntegerField()
    pin_2 = IntegerField()
    pin_20 = IntegerField()
    pin_21 = IntegerField()
    pin_22 = IntegerField()
    pin_23 = IntegerField()
    pin_24 = IntegerField()
    pin_25 = IntegerField()
    pin_26 = IntegerField()
    pin_27 = IntegerField()
    pin_28 = IntegerField()
    pin_29 = IntegerField()
    pin_3 = IntegerField()
    pin_30 = IntegerField()
    pin_31 = IntegerField()
    pin_32 = IntegerField()
    pin_33 = IntegerField()
    pin_34 = IntegerField()
    pin_35 = IntegerField()
    pin_36 = IntegerField()
    pin_37 = IntegerField()
    pin_38 = IntegerField()
    pin_39 = IntegerField()
    pin_4 = IntegerField()
    pin_40 = IntegerField()
    pin_41 = IntegerField()
    pin_42 = IntegerField()
    pin_43 = IntegerField()
    pin_44 = IntegerField()
    pin_45 = IntegerField()
    pin_46 = IntegerField()
    pin_47 = IntegerField()
    pin_48 = IntegerField()
    pin_49 = IntegerField()
    pin_5 = IntegerField()
    pin_50 = IntegerField()
    pin_51 = IntegerField()
    pin_52 = IntegerField()
    pin_53 = IntegerField()
    pin_54 = IntegerField()
    pin_55 = IntegerField()
    pin_56 = IntegerField()
    pin_57 = IntegerField()
    pin_58 = IntegerField()
    pin_59 = IntegerField()
    pin_6 = IntegerField()
    pin_60 = IntegerField()
    pin_61 = IntegerField()
    pin_62 = IntegerField()
    pin_63 = IntegerField()
    pin_64 = IntegerField()
    pin_65 = IntegerField()
    pin_66 = IntegerField()
    pin_67 = IntegerField()
    pin_68 = IntegerField()
    pin_69 = IntegerField()
    pin_7 = IntegerField()
    pin_70 = IntegerField()
    pin_71 = IntegerField()
    pin_72 = IntegerField()
    pin_73 = IntegerField()
    pin_74 = IntegerField()
    pin_75 = IntegerField()
    pin_76 = IntegerField()
    pin_77 = IntegerField()
    pin_78 = IntegerField()
    pin_79 = IntegerField()
    pin_8 = IntegerField()
    pin_80 = IntegerField()
    pin_81 = IntegerField()
    pin_82 = IntegerField()
    pin_83 = IntegerField()
    pin_84 = IntegerField()
    pin_85 = IntegerField()
    pin_86 = IntegerField()
    pin_87 = IntegerField()
    pin_88 = IntegerField()
    pin_89 = IntegerField()
    pin_9 = IntegerField()
    pin_90 = IntegerField()
    pin_91 = IntegerField()
    pin_92 = IntegerField()
    pin_93 = IntegerField()
    pin_94 = IntegerField()
    pin_95 = IntegerField()
    pin_96 = IntegerField()
    pin_97 = IntegerField()
    pin_98 = IntegerField()
    pin_99 = IntegerField()
    test_date = DateField()

    class Meta:
        db_table = 'ecu_data'

database.connect()                                                              # Connects to the db as database

# Tries to create the table and warns you if already exist
try:
    database.create_table(Ecu_data)
except OperationalError:
    print("Skipping ecu_data table creation. Table already exist")

################################################################################
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

adc.start_adc(0, gain=GAIN)

print('Reading ECU Pin ADC Values...')

ecu_test_current = Ecu_data()

ecu_test_current.db_ref = raw_input("DB Reference?: ")
ecu_test_current.ecu_ref = raw_input("ECU Reference?: ")
ecu_test_current.test_date = str(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
ecu_test_current.is_faulty = False

pin_list_instance = ['ecu_test_current.%s' % s for s in pin_list]               # Creates the list of pin_list to store the individual ADC average values

for i in tqdm(range(156)):
    meanvalue = []

    for a in range(10):
        adc_value = adc.get_last_result()
        time.sleep(0.005)
        meanvalue.append(adc_value)

    meanvaluesum = sum(meanvalue) / len (meanvalue)

    exec(str(pin_list_instance[i] + ' = ' + str(meanvaluesum)))                 # Basically it evaluates this function: 'ecu_test_current.pin_n = meanvaluesum' whereas 'n' is each pin iteration

ecu_test_current.save()

adc.stop_adc()
database.close()

###         - Klass object yaratish uchun shablon  -                 - Object - ma'lum klassning xususiy ko'rinishi -
#           ---------------------------------------                 ------------------------------------------------
#             
# 
#                    Avtomobil                                                  Avto 1
#               --------------------                                     -------------------------
#               -     model        -                                     - Model ="Malibu"       -
#               -     rang         -                                     - rang ="qora"          -
#               -     narh         -                                     - narh = 40000          -
#               --------------------                                     -------------------------
#               -     start()      -                                     -   start()             -
#               -     stop()       -                                     -   stop()              -
#               -     tezlash      -                                     -   tezlash()           -
#               --------------------                                     -------------------------
#
#
#
#
#                               INKAPSULYATSIYA                              ABSTRAKSIYA     
#                                ENCAPSULATION                               ABSTRACTION
#                                    ^                                          ^     
#                                    |                                          |
#                         O'zaro bog'liq ma'lumotlar va               Klassning ichki tuzilishi va    
#                          funksiyalarni birlashtirish                qanday ishlashini yashirish
#
#
#                                                    VORISLIK
#                                                   INHERITANCE
#                                                   |||||||||||
#
#
#                                                   TRANSPORT
#                                                 --------------
#                                                 - PROPERTIES -  --------> OTA (SUPER) klass
#                                                 --------------
#                                                 - METHODS    -
#                                                 --------------
#
#            AVTOMOBIL                  AVTOBUS                    KEMA                   POYEZD
#          --------------            --------------            --------------          --------------
#          - PROPERTIES -            - PROPERTIES -            - PROPERTIES -          - PROPERTIES -
#          --------------            --------------            --------------          --------------
#          - METHODS    -            -  METHODS   -            -  METHODS   -          -  METHODS   -
#          --------------            --------------            --------------          --------------
#                |                          |                         |                      |
#                |                          |                         |                      |
#                |                                                                           |
#                -----------------------------------------------------------------------------
#                                                         |
#                                                         |
#                                                   VORIS KLASSLAR
#                            Voris klasslar ota klassning ba'zi (yoki barcha) xususiyatlarini
#                                          va metodlarini meros qilib oladila
#
#
#                                                      POLIMORFIZM
#                                                      POLYMORPHISM
#                          Voris klass super klassdan o'zlashtirilgan metodning nomini saqlagan
#                               holda, uning ishlashini o'zgartirishga POLIMORFIZM deyiladi
#
#
#
#
#
#
#

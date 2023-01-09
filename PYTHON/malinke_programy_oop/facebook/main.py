from facebook import Facebook

petr = Facebook()
haryk = Facebook()
petr.jmeno = 'Petr Žůček'
haryk.jmeno = 'Jan Harenčák'
petr.vek = 26
haryk.vek = 26
petr.kamarad = haryk
haryk.kamarad = petr

petr.predstaveni()
haryk.predstaveni()

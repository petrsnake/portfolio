class Facebook():
    """
    třída lidí, co mají věk, jméno, kamaráda a umí se představit
    """
    jmeno = 'nezname'
    vek = 0
    kamarad = 'nezname'

    def predstaveni(self):
        """
        kazdy clen skupiny takto umí pozdravit
        """
        print(f'Ahoj, já jsem {self.jmeno}, je mi {self.vek} a můj kamarád je {self.kamarad.jmeno}.')
        print('Ahoj, já jsem {0}, je mi {1} a můj kamarád je {2}'.format(self.jmeno, self.vek, self.kamarad.jmeno))
from experta import *

"""
    The Following moods are actually numbers:
    1 --> Happy
    2 --> Sad
    3 --> Angry
    4 --> Heartbroken
"""
class MusicMood(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="music_mood")


    """
        The 1st Question that the user wants to answer
    """

    @Rule(Fact(action="music_mood"),
        NOT(Fact(feel=W())))
    def ask_feel(self):
        self.declare(Fact(feel=int(input("How do you Feel?" + 
                                    "\n1-Happy" +  
                                    "\n2-Sad" +
                                    "\n3-Angry" +
                                    "\n4-Heartbroken" + 
                                    "\n"))))


    """
        The 2nd Question
    """

    @Rule(Fact(action="music_mood"),
            Fact(feel=P(lambda x: x > 0) & P(lambda x: x <= 4)),
            NOT(Fact(musicType=W())))
    def r1(self):
        self.declare(Fact(musicType=int(input("What would you like to listen to?" + 
                                            "\n1-Vocal" +
                                            "\n2-Instrumental" +
                                            "\n3-Traditional"))))
    


    """
        Here is the section where the Expert system are asking a question
        to user of what type of songs you want to listen (Each section depends on
        the User's mood)
    """

    """
        The Happy Section
    """

    """
        For the Vocal songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=L(1)), # 1 -> Vocal
            NOT(Fact(specific=W())))
    def r11(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=L(1)), # 1 -> Vocal
            Fact(specific=L("y")))
    def r12(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=L(1)), # 1 -> Vocal
            Fact(specific=L("n")))
    def r13(self):
        None

    
    """
        For the Instrumental songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            NOT(Fact(specific=W())))
    def r21(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            Fact(specific=L("y")))
    def r22(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            Fact(specific=L("n")))
    def r23(self):
        None
    
    """
        For the Traditional songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=L(3)), # 3 -> Traditional
            NOT(Fact(specific=W())))
    def r31(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=MATCH.musicType), # 3 -> Traditional
            Fact(specific=L("y")))
    def r32(self, musicType):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=L(3)), # 3 -> Traditional
            Fact(specific=L("n")))
    def r33(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            NOT(Fact(isFeelBetter=W())))
    def n2(self):
        self.declare(Fact(isFeelBetter=input("Does that make you feel better? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            NOT(Fact(anotherSongs=W())))
    def r41(self):
        self.declare(Fact(anotherSongs=input("Do you want another happy song? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")))
    def r42(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            NOT(Fact(happyType=W())))
    def r43(self):
        self.declare(Fact(happyType=int(input("Are you :" + 
                                            "\n1-Trilled Happy" + 
                                            "\n2-Funky Happy"))))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(happyType=L(1)))
    def r44(self):
        print("suggest Sweet-Child-O-mine, We will Rock you, Nothing’s Gonna Stop Us Now")
        self.n2()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(happyType=L(2)))
    def r45(self):
        print("Suggest (Say yes, i Got you, up town Funk)")
        self.n2()
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            NOT(Fact(isFeelDifferent=W())))
    def r51(self):
        self.declare(Fact(isFeelDifferent=input("Do you feel different? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            NOT(Fact(anotherFeeling=W())))
    def r52(self):
        self.declare(Fact(anotherFeeling=input("Do you want to add another feeling? (Y/N)")))

    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            NOT(Fact(addedAnotherFeeling=W())))
    def r53(self):
        self.declare(Fact(addedAnotherFeeling=int(input("What feeling do you want to add?" + 
                                                    "\n1- Sad" +
                                                    "\n2- Angry" + 
                                                    "\n3- Heartbroken \n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1)),
            NOT(Fact(originalOrNewFeeling=W())))
    def r54(self):
        self.declare(Fact(originalOrNewFeeling=int(input("Which feeling you tend to feel more?" + 
                                                    "\n1- The original" +
                                                    "\n2- New Added feeling \n"))))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1)),
            Fact(originalOrNewFeeling=L(1)),
            NOT(Fact(continuePlaying=W())))
    def r55(self):
        print("suggest November rain, Bohemian Rhapsody")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1)),
            Fact(originalOrNewFeeling=L(2)),
            NOT(Fact(continuePlaying=W())))
    def r56(self):
        print("suggest Stairway To Heaven, dark Side of the moon")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            NOT(Fact(lessOrMore=W())))
    def r57(self):
        self.declare(Fact(lessOrMore=int(input("Are you: \n1-Less happy \n2-More happy\n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            NOT(Fact(changeToSad=W())))
    def r58(self):
        self.declare(Fact(changeToSad=input("Do you want to change the feeling to sad? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToSad=L("y")))
    def r59(self):
        None
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            NOT(Fact(isInLove=W())))
    def r60(self):
        self.declare(Fact(isInLove=input("Are you in love? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(isInLove=L("y")))
    def r61(self):
        print("suggest I Gotta Feeling, Love On Top, Can't Stop the Feeling!")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            NOT(Fact(addAnotherSong=W())))
    def r62(self):
        self.declare(Fact(addAnotherSong=input("Do you want another song? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(addAnotherSong=L("y")))
    def r63(self):
        print("Play Happy by Pharrell Williams")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(addAnotherSong=L("n")),
            NOT(Fact(isFeelDifferent=W())))
    def r64(self):
        self.declare(Fact(isFeelDifferent=input("Do you feel different? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            NOT(Fact(anotherFeeling=W())))
    def r67(self):
        self.declare(Fact(anotherFeeling=input("Do you want to add another feeling? (Y/N)")))

    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            NOT(Fact(addedAnotherFeeling=W())))
    def r68(self):
        self.declare(Fact(addedAnotherFeeling=int(input("What feeling do you want to add?" + 
                                                    "\n1- Sad" +
                                                    "\n2- Angry" + 
                                                    "\n3- Heartbroken \n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            NOT(Fact(originalOrNewFeeling=W())))
    def r69(self):
        self.declare(Fact(originalOrNewFeeling=int(input("Which feeling you tend to feel more?" + 
                                                    "\n1- The original" +
                                                    "\n2- New Added feeling \n"))))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1)),
            Fact(originalOrNewFeeling=L(1)),
            NOT(Fact(continuePlaying=W())))
    def r70(self):
        print("suggest You’re My Best Friend, River of Dreams, Sunday Morning, Eye of the Tiger")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1)),
            Fact(originalOrNewFeeling=L(2)),
            NOT(Fact(continuePlaying=W())))
    def r71(self):
        print("suggest All I Wanna Do, Don't Worry, Be Happy, My Immortal")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            NOT(Fact(lessOrMore=W())))
    def r72(self):
        self.declare(Fact(lessOrMore=int(input("Are you: \n1-Less happy \n2-More happy\n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            NOT(Fact(changeToSad=W())))
    def r73(self):
        self.declare(Fact(changeToSad=input("Do you want to change the feeling to sad? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToSad=L("y")))
    def r74(self):
        None
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            NOT(Fact(isInLove=W())))
    def r75(self):
        self.declare(Fact(isInLove=input("Are you in love? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(isInLove=L("y")))
    def r76(self):
        print("suggest I’m A Believer, I Want To Hold Your Hand, It's a Great Day to Be Alive")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(1)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y") | L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1)),
            Fact(originalOrNewFeeling=L(1) | L(2)),
            Fact(continuePlaying=L("y")))
    def r77(self):
        None

    """
        The end of Happy section
    """

    """
        The Sad Session
    """
    """
        For the Vocal songs
    """

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=L(1)), # 1 -> Vocal
            NOT(Fact(specific=W())))
    def r78(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=L(1)), # 1 -> Vocal
            Fact(specific=L("y")))
    def r79(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=L(1)), # 1 -> Vocal
            Fact(specific=L("n")))
    def r80(self):
        None

    
    """
        For the Instrumental songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            NOT(Fact(specific=W())))
    def r81(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            Fact(specific=L("y")))
    def r82(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            Fact(specific=L("n")))
    def r83(self):
        None
    
    """
        For the Traditional songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=L(3)), # 3 -> Traditional
            NOT(Fact(specific=W())))
    def r84(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=MATCH.musicType), # 3 -> Traditional
            Fact(specific=L("y")))
    def r85(self, musicType):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=L(3)), # 3 -> Traditional
            Fact(specific=L("n")))
    def r86(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            NOT(Fact(isFeelBetter=W())))
    def r87(self):
        self.declare(Fact(isFeelBetter=input("Does that make you feel better? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            NOT(Fact(anotherSongs=W())))
    def m2(self):
        self.declare(Fact(anotherSongs=input("Do you want another sad song? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            NOT(Fact(continuePlaying=W())))
    def m3(self):
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=W()),
            NOT(Fact(isCalmSad=W())))
    def r90(self):
        self.declare(Fact(isCalmSad=input("Are you calm sad? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("y")),
            Fact(isCalmSad=L("y")))
    def r91(self):
        print("Play the Boxer")
        self.m2()
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("y")),
            Fact(isCalmSad=L("n")))
    def r92(self):
        print("Play wish way you are")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("n")),
            NOT(Fact(isAngrySad=W())))
    def r93(self):
        self.declare(Fact(isAngrySad=input("Are you Angry sad? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("n")),
            Fact(isAngrySad=L("y")))
    def r94(self):
        print("play Let it rain by sarah Bokson")
        self.m2()
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("n")),
            Fact(isAngrySad=L("n")))
    def r95(self):
        print("suggest a song from dataset")
        self.m3()
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            NOT(Fact(isFeelDifferent=W())))
    def r96(self):
        self.declare(Fact(isFeelDifferent=input("Do you feel different? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("y")))
    def r97(self):
        self.r1()
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            NOT(Fact(anotherFeeling=W())))
    def r98(self):
        self.declare(Fact(anotherFeeling=input("Do you want to add another feeling? (Y/N)")))

    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            NOT(Fact(addedAnotherFeeling=W())))
    def r99(self):
        self.declare(Fact(addedAnotherFeeling=int(input("What feeling do you want to add?" + 
                                                    "\n1- Happy" +
                                                    "\n2- Angry" + 
                                                    "\n3- Heartbroken \n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            NOT(Fact(originalOrNewFeeling=W())))
    def r100(self):
        self.declare(Fact(originalOrNewFeeling=int(input("Which feeling you tend to feel more?" + 
                                                    "\n1- The original" +
                                                    "\n2- New Added feeling \n"))))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            NOT(Fact(continuePlaying=W())))
    def r101(self):
        print("play gloomy sunday")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("y")),
            NOT(Fact(likeIt=W())))
    def k2(self):
        print("play ala el ghobra")
        self.declare(Fact(likeIt=input("Like it? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("y")),
            Fact(likeIt=L("y")))
    def r122(self):
        print("play yanadmana")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("y")),
            Fact(likeIt=L("n")))
    def r123(self):
        self.k1()
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("n")),
            NOT(Fact(somethingFresh=W())))
    def k1(self):
        self.declare(Fact(somethingFresh=input("wanna something fresh? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("n")),
            Fact(somethingFresh=L("y")))
    def r125(self):
        print("play i like it i love it")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("n")),
            Fact(somethingFresh=L("n")))
    def r126(self):
        self.k2()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            NOT(Fact(continuePlaying=W())))
    def r127(self):
        print("play can we kiss forever")
        self.declare(Fact(continuePlaying=input("continue playing? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            NOT(Fact(likeIt=W())))
    def r128(self):
        print("play river of dreams")
        self.declare(Fact(likeIt=input("Like it? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            Fact(likeIt=L("y")))
    def r129(self):
        print("play I am a beliver")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            Fact(likeIt=L("n")))
    def r129(self):
        print("play U suck man")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            NOT(Fact(lessOrMore=W())))
    def r130(self):
        self.declare(Fact(lessOrMore=int(input("Are you: \n1-Less sad \n2-More sad\n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            NOT(Fact(changeToHappy=W())))
    def r131(self):
        self.declare(Fact(changeToHappy=input("Do you want to change the feeling to happy? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("y")))
    def r132(self):
        print("change feeling to happy")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            NOT(Fact(changetoHeartBroken=W())))
    def r133(self):
        self.declare(Fact(changetoHeartBroken=input("Are you heartbroken? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(changetoHeartBroken=L("y")))
    def r134(self):
        print("change to heartbroken")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(changetoHeartBroken=L("n")))
    def r135(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            NOT(Fact(anotherSongs=W())))
    def r136(self):
        self.declare(Fact(anotherSongs=input("Do you want another sad song? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("y")),
            NOT(Fact(continuePlaying=W())))
    def r137(self):
        None
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            NOT(Fact(isFeelDifferent=W())))
    def r138(self):
        self.declare(Fact(isFeelDifferent=input("Do you feel different? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("y")))
    def r139(self):
        self.r1()
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            NOT(Fact(anotherFeeling=W())))
    def r140(self):
        self.declare(Fact(anotherFeeling=input("Do you want to add another feeling? (Y/N)")))

    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            NOT(Fact(addedAnotherFeeling=W())))
    def r141(self):
        self.declare(Fact(addedAnotherFeeling=int(input("What feeling do you want to add?" + 
                                                    "\n1- Happy" +
                                                    "\n2- Angry" + 
                                                    "\n3- Heartbroken \n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            NOT(Fact(originalOrNewFeeling=W())))
    def r142(self):
        self.declare(Fact(originalOrNewFeeling=int(input("Which feeling you tend to feel more?" + 
                                                    "\n1- The original" +
                                                    "\n2- New Added feeling \n"))))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            NOT(Fact(continuePlaying=W())))
    def r143(self):
        print("play clouds")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("y")),
            NOT(Fact(likeIt=W())))
    def r144(self):
        print("play no names")
        self.declare(Fact(likeIt=input("Like it? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("y")),
            Fact(likeIt=L("y")))
    def r144(self):
        print("Play old sheep")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("y")),
            Fact(likeIt=L("n")))
    def r145(self):
        print("idk man u really bad")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("n")),
            NOT(Fact(somethingFresh=W())))
    def r146(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            NOT(Fact(continuePlaying=W())))
    def r149(self):
        print("castle of sand")
        self.declare(Fact(continuePlaying=input("continue playing? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            NOT(Fact(likeIt=W())))
    def r150(self):
        print("play sunday mornings")
        self.declare(Fact(likeIt=input("Like it? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            Fact(likeIt=L("y")))
    def r151(self):
        print("play you r my best friend")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            Fact(likeIt=L("n")))
    def r151(self):
        print("KYS")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            NOT(Fact(lessOrMore=W())))
    def r152(self):
        self.declare(Fact(lessOrMore=int(input("Are you: \n1-Less sad \n2-More sad\n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            NOT(Fact(changeToHappy=W())))
    def r153(self):
        self.declare(Fact(changeToHappy=input("Do you want to change the feeling to happy? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("y")))
    def r154(self):
        print("change feeling to happy")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            NOT(Fact(changetoHeartBroken=W())))
    def r155(self):
        self.declare(Fact(changetoHeartBroken=input("Are you heartbroken? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(changetoHeartBroken=L("y")))
    def r156(self):
        print("change to heartbroken")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(2)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(changetoHeartBroken=L("n")))
    def r157(self):
        None

    """
        The end of Sad session
    """

    """
        The Angry Session
    """

    """
        For the Vocal songs
    """

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=L(1)), # 1 -> Vocal
            NOT(Fact(specific=W())))
    def r158(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=L(1)), # 1 -> Vocal
            Fact(specific=L("y")))
    def r159(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=L(1)), # 1 -> Vocal
            Fact(specific=L("n")))
    def r160(self):
        None

    
    """
        For the Instrumental songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            NOT(Fact(specific=W())))
    def r161(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            Fact(specific=L("y")))
    def r162(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            Fact(specific=L("n")))
    def r163(self):
        None
    
    """
        For the Traditional songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=L(3)), # 3 -> Traditional
            NOT(Fact(specific=W())))
    def r164(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=MATCH.musicType), # 3 -> Traditional
            Fact(specific=L("y")))
    def r164(self, musicType):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=L(3)), # 3 -> Traditional
            Fact(specific=L("n")))
    def r165(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            NOT(Fact(isFeelBetter=W())))
    def r166(self):
        self.declare(Fact(isFeelBetter=input("Does that make you feel better? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            NOT(Fact(anotherSongs=W())))
    def t2(self):
        self.declare(Fact(anotherSongs=input("Do you want another Angry song? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            NOT(Fact(continuePlaying=W())))
    def r168(self):
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("y")),
            NOT(Fact(feelSoBad=W())))
    def r169(self):
        print("play lost frequencies")
        self.declare(Fact(feelSoBad=input("Wanna feel so bad? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("y")),
            Fact(feelSoBad=L("y")))
    def r170(self):
        print("play Hammer smashed face")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("y")),
            Fact(feelSoBad=L("n")),
            NOT(Fact(continuePlaying1=W())))
    def r171(self):
        self.declare(Fact(continuePlaying1=input("continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("y")),
            Fact(feelSoBad=L("n")),
            Fact(continuePlaying1=L("y")))
    def r172(self):
        print("play only love by neil strong")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("y")),
            Fact(feelSoBad=L("n")),
            Fact(continuePlaying1=L("n")))
    def r173(self):
        self.t2();

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(continuePlaying=L("n")))
    def r167(self):
        self.declare(Fact(anotherSongs=None))
        self.t2();

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("y")))
    def r174(self):
        print("play nothing gonna stop us")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            NOT(Fact(anotherFeeling=W())))
    def r175(self):
        self.declare(Fact(anotherFeeling=input("Do you want to add another feeling? (Y/N)")))

    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            NOT(Fact(addedAnotherFeeling=W())))
    def r176(self):
        self.declare(Fact(addedAnotherFeeling=int(input("What feeling do you want to add?" + 
                                                    "\n1- Sad" +
                                                    "\n2- Happy" + 
                                                    "\n3- Heartbroken \n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            NOT(Fact(originalOrNewFeeling=W())))
    def r177(self):
        self.declare(Fact(originalOrNewFeeling=int(input("Which feeling you tend to feel more?" + 
                                                    "\n1- The original" +
                                                    "\n2- New Added feeling \n"))))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            NOT(Fact(continuePlaying=W())))
    def r178(self):
        print("play chapel of ghouls by morbid angel")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("y")))
    def r179(self):
        print("play the little girl")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(continuePlaying=L("n")))
    def r180(self):
        self.declare(Fact(anotherSongs=None))
        self.t2()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            NOT(Fact(continuePlaying=W())))
    def r181(self):
        print("play what is love by lost frequencies")
        self.declare(Fact(continuePlaying=input("continue playing? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")))
    def r181(self):
        print("play save me by Queen")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("n")),
            NOT(Fact(feelDifferent=W())))
    def r182(self):
        self.declare(Fact(feelDifferent=input("wanna feel different? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("n")),
            Fact(feelDifferent=L("y")),
            NOT(Fact(likeIt=W())))
    def r183(self):
        print("play bohemian Rhapsody")
        self.declare(Fact(likeIt=input("Like that? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("n")),
            Fact(feelDifferent=L("y")),
            Fact(likeIt=L("y")))
    def r184(self):
        print("play love on top")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("n")),
            Fact(feelDifferent=L("y")),
            Fact(likeIt=L("n")))
    def r185(self):
        self.declare(Fact(anotherSongs=None))
        self.t2()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("n")),
            Fact(feelDifferent=L("n")),
            NOT(Fact(likeIt=W())))
    def r186(self):
        print("play i gotta feeling ")
        self.declare(Fact(likeIt=input("Like that? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(likeIt=L("y")))
    def r187(self):
        print("play here comes the sun")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(likeIt=L("n")))
    def r188(self):
        self.declare(Fact(anotherSongs=None))
        self.t2()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            NOT(Fact(lessOrMore=W())))
    def r189(self):
        self.declare(Fact(lessOrMore=int(input("Are you: \n1-Less angry \n2-More angry\n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            NOT(Fact(changeToHappy=W())))
    def r190(self):
        self.declare(Fact(changeToHappy=input("Do you want to change the feeling to happy? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("y")))
    def r191(self):
        print("change feeling to happy")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            NOT(Fact(changetoSad=W())))
    def r192(self):
        self.declare(Fact(changetoSad=input("Are you sad? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(changetoSad=L("y")))
    def r193(self):
        print("change feeling to sad")
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(changetoSad=L("n")))
    def r194(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            NOT(Fact(anotherSongs=W())))
    def r195(self):
        self.declare(Fact(anotherSongs=input("Do you want another sad song? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            NOT(Fact(isFeelDifferent=W())))
    def r196(self):
        self.declare(Fact(isFeelDifferent=input("Do you feel different? (Y/N)")))

    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            NOT(Fact(anotherFeeling=W())))
    def r197(self):
        self.declare(Fact(anotherFeeling=input("Do you want to add another feeling? (Y/N)")))

    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            NOT(Fact(addedAnotherFeeling=W())))
    def r198(self):
        self.declare(Fact(addedAnotherFeeling=int(input("What feeling do you want to add?" + 
                                                    "\n1- Sad" +
                                                    "\n2- Happy" + 
                                                    "\n3- Heartbroken \n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            NOT(Fact(originalOrNewFeeling=W())))
    def r199(self):
        self.declare(Fact(originalOrNewFeeling=int(input("Which feeling you tend to feel more?" + 
                                                    "\n1- The original" +
                                                    "\n2- New Added feeling \n"))))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            NOT(Fact(moreThanThat=W())))
    def w8(self):
        print("play Useless sacrifice by Death Decline")
        self.declare(Fact(moreThanThat=input("Wanna more like that? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(moreThanThat=L("y")),
            NOT(Fact(likeIt=W())))
    def r201(self):
        print("play nothing else matters")
        self.declare(Fact(likeIt=input("more? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(moreThanThat=L("y")),
            Fact(likeIt=L("y")))
    def r202(self):
        print("play whiskey in jar")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(moreThanThat=L("y")),
            Fact(likeIt=L("n")))
    def r203(self):
        self.declare(moreThanThat=None)
        self.declare(likeit=None)
        self.w8()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(moreThanThat=L("n")),
            NOT(Fact(isMore=W())))
    def r204(self):
        print("play here comes the sun")
        self.declare(Fact(isMore=input("More? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(moreThanThat=L("y")),
            Fact(isMore=L("y")))
    def r205(self):
        print("play the litte girl")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(1)),
            Fact(moreThanThat=L("y")),
            Fact(isMore=L("n")))
    def r206(self):
        self.declare(moreThanThat=None)
        self.declare(likeit=None)
        self.w8()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            NOT(Fact(continuePlaying=W())))
    def x4(self):
        print("play live your life by IT")
        self.declare(Fact(continuePlaying=input("continue playing? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            NOT(Fact(isMore=W())))
    def r208(self):
        print("play dancing in a burning room")
        self.declare(Fact(isMore=input("More? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            Fact(isMore=L("y")))
    def r209(self):
        print("play the litte girl")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("y")),
            Fact(addedAnotherFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNewFeeling=L(2)),
            Fact(continuePlaying=L("y")),
            Fact(isMore=L("n")))
    def r210(self):
        self.x4()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            NOT(Fact(lessOrMore=W())))
    def r211(self):
        self.declare(Fact(lessOrMore=int(input("Are you: \n1-Less angry \n2-More angry\n"))))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            NOT(Fact(changeToHappy=W())))
    def r212(self):
        self.declare(Fact(changeToHappy=input("Do you want to change the feeling to happy? (Y/N)")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("y")),
            NOT(Fact(isMore1=W())))
    def r213(self):
        print("play love on top")
        self.declare(Fact(isMore1=input("More? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("y")),
            Fact(isMore1=L("y")))
    def r214(self):
        print("play don't stop believing")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("y")),
            Fact(isMore1=L("n")))
    def r215(self):
        self.x4()

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("n")),
            NOT(Fact(isMore1=W())))
    def r216(self):
        print("play i got you")
        self.declare(Fact(isMore1=input("More? (Y/N)")))

    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("n")),
            Fact(isMore1=L("y")))
    def r217(self):
        print("play stronger")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(1)),
            Fact(changeToHappy=L("n")),
            Fact(isMore1=L("n")))
    def r218(self):
        self.x4()
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            NOT(Fact(changetoSad=W())))
    def r219(self):
        self.declare(Fact(changetoSad=input("Are you sad? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(3)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(isFeelDifferent=L("n")),
            Fact(anotherFeeling=L("n")),
            Fact(lessOrMore=L(2)),
            Fact(changetoSad=L("y")))
    def r220(self):
        print("change to sad")

    """
        The end of Angry session
    """

    """
        The Heartbroken Session
    """

    
    """
        For the Vocal songs
    """

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=L(1)), # 1 -> Vocal
            NOT(Fact(specific=W())))
    def r300(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=L(1)), # 1 -> Vocal
            Fact(specific=L("y")))
    def r301(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=L(1)), # 1 -> Vocal
            Fact(specific=L("n")))
    def r302(self):
        None

    
    """
        For the Instrumental songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            NOT(Fact(specific=W())))
    def r303(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            Fact(specific=L("y")))
    def r304(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=L(2)), # 2 -> Instrumental
            Fact(specific=L("n")))
    def r305(self):
        None
    
    """
        For the Traditional songs
    """
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=L(3)), # 3 -> Traditional
            NOT(Fact(specific=W())))
    def r306(self):
        self.declare(Fact(specific=input("is there anything specific? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=MATCH.musicType), # 3 -> Traditional
            Fact(specific=L("y")))
    def r307(self, musicType):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=L(3)), # 3 -> Traditional
            Fact(specific=L("n")))
    def r308(self):
        None

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            NOT(Fact(isFeelBetter=W())))
    def r309(self):
        self.declare(Fact(isFeelBetter=input("Does that make you feel better? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            NOT(Fact(anotherSongs=W())))
    def r310(self):
        self.declare(Fact(anotherSongs=input("Do you want another Heartbroken song? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            NOT(Fact(feelDifferent=W())))
    def r311(self):
        print("play omri bm7btk lost")
        self.declare(Fact(feelDifferent=input("Do you feel different? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            NOT(Fact(addAnotherFeeling=W())))
    def r312(self):
        self.declare(Fact(addAnotherFeeling=input("Do you want to add another feeling? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            NOT(Fact(addedFeeling=W())))
    def r329(self):
        self.declare(Fact(addedFeeling=input("What feeling do you want to add? \n1-Sad \n2-Angry \n3-Happy")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            NOT(Fact(originalOrNew=W())))
    def r313(self):
        self.declare(Fact(originalOrNew=input("Which feeling you tend to feel more? \n1- The original \n 2- new added feeling")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("1")),
            NOT(Fact(continuePlaying=W())))
    def r314(self):
        print("play Sad iraqi songs")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("1")),
            Fact(continuePlaying=L("y")),
            NOT(Fact(continuePlaying1=W())))
    def r315(self):
        print("play I will survive")
        self.declare(Fact(continuePlaying1=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("1")),
            Fact(continuePlaying=L("y")),
            Fact(continuePlaying1=W("y")))
    def r316(self):
        print("play babe i am gonna leave you")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("1")),
            Fact(continuePlaying=L("y")),
            Fact(continuePlaying1=W("n")),
            NOT(Fact(suggestSomething=W())))
    def r317(self):
        self.declare(suggestSomething=input("suggest something cool? (Y/N)"))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("1")),
            Fact(continuePlaying=L("y")),
            Fact(continuePlaying1=W("n")),
            Fact(suggestSomething=L("y")))
    def r318(self):
        print("play sweet child \'o mine")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("1")),
            Fact(continuePlaying=L("y")),
            Fact(continuePlaying1=W("n")),
            Fact(suggestSomething=L("n")))
    def r319(self):
        print("play gloomy sunday")


    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("2")),
            NOT(Fact(continuePlaying=W())))
    def r320(self):
        print("play Happy BY pharrel williams")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("2")),
            Fact(continuePlaying=L("y")),
            NOT(Fact(continuePlaying1=W())))
    def r321(self):
        print("play stairway to hevean")
        self.declare(Fact(continuePlaying1=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("2")),
            Fact(continuePlaying=L("y")),
            Fact(continuePlaying1=W("y")))
    def r322(self):
        print("play uptown funk")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("2")),
            Fact(continuePlaying=L("y")),
            Fact(continuePlaying1=W("n")))
    def r323(self):
        print("play tears in heaven")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            NOT(Fact(lessOrMore=W())))
    def r324(self):
        self.declare(Fact(lessOrMore=input("Are you? \n1- less heartbroken \n2- more heartbroken")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            Fact(lessOrMore=L("1")),
            NOT(Fact(changeToHappy=W())))
    def r325(self):
        self.declare(Fact(changeToHappy=input("Want to change to Happy? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            Fact(lessOrMore=L("1")),
            Fact(changeToHappy=L("y")))
    def r326(self):
        print("Change feeling to Happy")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            Fact(lessOrMore=L("2")),
            NOT(Fact(changeToSad=W())))
    def r327(self):
        self.declare(Fact(changeToHappy=input("Are you Sad? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("y")),
            Fact(anotherSongs=L("y")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            Fact(lessOrMore=L("2")),
            Fact(changeToSad=L("y")))
    def r328(self):
        print("Change feeling to Sad")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            NOT(Fact(anotherSongs=W())))
    def r335(self):
        self.declare(Fact(anotherSongs=input("Do you want another Heartbroken song? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            NOT(Fact(feelDifferent=W())))
    def r330(self):
        self.declare(Fact(feelDifferent=input("Do you feel different? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            NOT(Fact(addAnotherFeeling=W())))
    def r331(self):
        self.declare(Fact(addAnotherFeeling=input("Do you want to add another feeling? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            NOT(Fact(addedFeeling=W())))
    def r332(self):
        self.declare(Fact(addedFeeling=int(input("What feeling do you want to add? \n1-Sad \n2-Angry \n3-Happy"))))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            NOT(Fact(originalOrNew=W())))
    def r333(self):
        self.declare(Fact(originalOrNew=input("Which feeling you tend to feel more? \n1- The original \n 2- new added feeling")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("1")),
            NOT(Fact(continuePlaying=W())))
    def r334(self):
        print("play november rain by gunz n roses")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))


    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("y")),
            Fact(addedFeeling=L(1) | L(2) | L(3)),
            Fact(originalOrNew=L("2")),
            NOT(Fact(continuePlaying=W())))
    def r336(self):
        print("play i got feeling by will i am")
        self.declare(Fact(continuePlaying=input("Continue playing? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            NOT(Fact(lessOrMore=W())))
    def r337(self):
        self.declare(Fact(lessOrMore=input("Are you? \n1- less heartbroken \n2- more heartbroken")))
    
    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            Fact(lessOrMore=L("1")),
            NOT(Fact(changeToHappy=W())))
    def r338(self):
        self.declare(Fact(changeToHappy=input("Want to change to Happy? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            Fact(lessOrMore=L("1")),
            Fact(changeToHappy=L("y")))
    def r339(self):
        print("Change feeling to Happy")

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            Fact(lessOrMore=L("2")),
            NOT(Fact(changeToSad=W())))
    def r340(self):
        self.declare(Fact(changeToHappy=input("Are you Sad? (Y/N)")))

    @Rule(Fact(action="music_mood"),
            Fact(feel=L(4)),
            Fact(musicType=P(lambda x: x > 0) & P(lambda x: x <= 3)),
            Fact(specific=L("n")),
            Fact(isFeelBetter=L("n")),
            Fact(anotherSongs=L("n")),
            Fact(feelDifferent=L("n")),
            Fact(addAnotherFeeling=L("n")),
            Fact(lessOrMore=L("2")),
            Fact(changeToSad=L("y")))
    def r341(self):
        print("Change feeling to Sad")
    

    """
        The end of heartbroken session
    """
    
    
    
    


engine = MusicMood()

while (1):
    engine.reset()
    engine.run()

    if input("Continue questioning? (Y/N)") == "n":
        break
    
engine.facts
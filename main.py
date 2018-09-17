import wx, random, pyperclip as pc

class App(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, ' RGB2HEX', size=(350, 500), style=wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX)
        self.bg = self.generateRandomColour()
        self.favicon = wx.Icon('./assets/r2h.png', wx.BITMAP_TYPE_PNG, 32, 32)
        self.SetIcon(self.favicon)
        self.CreateStatusBar(1)
        self.StatusBar.SetStatusText(' Developed with Love by @majiyd_ ')

        self.mainPanel = wx.Panel(self, -1)
        self.mainPanel.SetBackgroundColour(self.bg)
        self.mainPanelSizer = wx.GridBagSizer(0, 0)
        font = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'consolas')

        self.rgbPanel = wx.Panel(self.mainPanel, -1)
        self.rText = wx.StaticText(self.rgbPanel, -1, 'R: ', pos=(20, 30))
        self.rText.SetFont(font)
        self.rTc = wx.TextCtrl(self.rgbPanel, -1, pos=(50, 30), size = (48, 32))
        self.rTc.SetFont(font)
        self.rTc.SetMaxLength(3)

        self.gText = wx.StaticText(self.rgbPanel, -1, 'G: ', pos=(110, 30))
        self.gText.SetFont(font)
        self.gTc = wx.TextCtrl(self.rgbPanel, -1, pos=(140, 30), size=(48, 32))
        self.gTc.SetFont(font)
        self.gTc.SetMaxLength(3)
        self.bText = wx.StaticText(self.rgbPanel, -1, 'B: ', pos=(210, 30))
        self.bText.SetFont(font)
        self.bTc = wx.TextCtrl(self.rgbPanel, -1, pos=(235, 30), size=(48, 32))
        self.bTc.SetFont(font)
        self.bTc.SetMaxLength(3)
        self.conversionMechanism(self.bg)
        self.copyRGB = wx.BitmapButton(self.rgbPanel, -1, wx.Bitmap('./assets/paste3.png'),
                                       style=wx.NO_BORDER, pos=(300, 35))
        self.copyRGB.SetToolTipString('Copy RGB Colour')

        self.mainPanelSizer.Add(self.rgbPanel, (0, 0), (1, 10), wx.TOP, 20)



        self.hexPanel = wx.Panel(self.mainPanel, -1)
        self.hexText = wx.StaticText(self.hexPanel, -1, 'HEX: ', pos=(30, 40))
        self.hexText.SetFont(font)
        self.hexTc = wx.TextCtrl(self.hexPanel, -1, pos=(120, 35), size=(96, 32))
        self.hexTc.SetFont(font)
        self.hexTc.SetMaxLength(6)
        self.hexTc.SetValue(self.bg.lstrip('#').upper())
        self.copyHex = wx.BitmapButton(self.hexPanel, -1, wx.Bitmap('./assets/paste3.png'),
                                        style=wx.NO_BORDER, pos=(250, 42))
        self.copyHex.SetToolTipString('Copy HEX colour')
        self.mainPanelSizer.Add(self.hexPanel, (1, 0), (1, 10), wx.EXPAND | wx.BOTTOM, 120)


        self.otherPanel = wx.Panel(self.mainPanel, -1)
        self.newColourButton = wx.BitmapButton(self.mainPanel, -1, wx.Bitmap('./assets/refresh.png'),  pos=(150, 260))
        self.newColourButton.SetToolTipString('Generate New Colour')
        self.mainPanelSizer.Add(self.otherPanel, (2, 0), (3, 10), wx.EXPAND | wx.BOTTOM, 40)


        self.mainPanelSizer.AddGrowableRow(0)
        self.mainPanelSizer.AddGrowableCol(0)
        self.mainPanelSizer.AddGrowableRow(1)
        self.mainPanelSizer.AddGrowableRow(2)
        self.mainPanel.SetSizerAndFit(self.mainPanelSizer)

        self.Bind(wx.EVT_BUTTON, self.onClickNewColourButton, self.newColourButton)
        self.hexTc.Bind(wx.EVT_KEY_UP, self.convertHexToRgb)
        self.rTc.Bind(wx.EVT_KEY_UP, self.convertRgbToHex)
        self.gTc.Bind(wx.EVT_KEY_UP, self.convertRgbToHex)
        self.bTc.Bind(wx.EVT_KEY_UP, self.convertRgbToHex)
        self.Bind(wx.EVT_BUTTON, self.onCopyRGB, self.copyRGB)
        self.Bind(wx.EVT_BUTTON, self.onCopyHex, self.copyHex)
        # self.Centre()
        self.Move((150, 150))
        self.Show(True)

        

    def generateRandomColour(self):
        self.usables = '0123456789ABCDEF'
        randomColour = '#'
        for _ in range(6):
            randomColour+=random.choice(self.usables)
        return randomColour

    def onClickNewColourButton(self, event):
        self.bg = self.generateRandomColour()
        self.mainPanel.SetBackgroundColour(self.bg)
        self.hexTc.SetValue(self.bg.lstrip('#').upper())
        self.conversionMechanism(self.bg)
        self.Refresh()

    def convertHexToRgb(self, event):
        self.hex = self.hexTc.GetValue()

        if(self.hex != ''):
            if self.hex[-1].upper() not in self.usables:
                self.hexTc.SetValue(self.hexTc.GetValue()[:-1])
                self.hexTc.SetInsertionPointEnd()

        if (len(self.hexTc.GetValue()) == 6):
            self.conversionMechanism(self.hexTc.GetValue())
            self.mainPanel.SetBackgroundColour('#'+self.hexTc.GetValue())
            self.Refresh()

        elif (len(self.hexTc.GetValue()) == 3):
            self.hexc = self.hexTc.GetValue()
            retcolor ='#'
            for ch in self.hexc:
                retcolor+=(ch*2)

            self.conversionMechanism(retcolor)
            self.mainPanel.SetBackgroundColour(retcolor)
            self.Refresh()



            #print(int(self.hex, 16))
    def conversionMechanism(self, hexColour):
        hexColour = hexColour.lstrip('#')
        try:
            rhex = hexColour[0:2]
            self.r = str(int(rhex, 16))
            ghex = hexColour[2:4]
            self.g = str(int(ghex, 16))
            bhex = hexColour[4:6]
            self.b = str(int(bhex, 16))

            self.rTc.SetValue(self.r)
            self.gTc.SetValue(self.g)
            self.bTc.SetValue(self.b)
        except:
            pass

    def convertRgbToHex(self, event):
        r = self.rTc.GetValue()
        g = self.gTc.GetValue()
        b = self.bTc.GetValue()
        if ((r != '') and (g != '') and (b != '')):
            if (r.isdigit() and g.isdigit() and b.isdigit()):
                if (int(r) < 256 and int(g) < 256 and int(b) < 256):
                    self.rgb2hexConversion( r, g, b)
                elif int(r) > 255:
                    self.rTc.SetValue(self.r)
                    self.rTc.SetInsertionPointEnd()
                elif int(g) > 255:
                    self.gTc.SetValue(self.g)
                    self.gTc.SetInsertionPointEnd()
                elif int(b) > 255:
                    self.bTc.SetValue(self.b)
                    self.bTc.SetInsertionPointEnd()

            else:
                if not r.isdigit():
                    self.setToNumber(self.rTc, r)

                elif not g.isdigit():
                    self.setToNumber(self.gTc, g)

                elif not b.isdigit():
                    self.setToNumber(self.bTc, b)


    def setToNumber(self, textCtrl, value):
        cleanNumber =''
        for ch in value:
            if ch.isdigit():
                cleanNumber+=ch

        textCtrl.SetValue(cleanNumber)
        textCtrl.SetInsertionPointEnd()

    def rgb2hexConversion(self, r, g, b):
        returnHex = '#'
        self.r = self.rTc.GetValue()
        self.g = self.gTc.GetValue()
        self.b = self.bTc.GetValue()
        rhex, ghex, bhex =((hex(int(r)).lstrip('0x')), hex(int(g)).lstrip('0x'), hex(int(b)).lstrip('0x'))
        if len(rhex) < 2:
            rhex='0'+rhex


        if len(ghex) < 2:
            ghex = '0' + ghex

        if len(bhex) < 2:
            bhex = '0' + bhex

        rhex = '00' if rhex == '0' else rhex
        ghex = '00' if ghex == '0' else ghex
        bhex = '00' if bhex == '0' else bhex
        returnHex += rhex
        returnHex += ghex
        returnHex += bhex

        self.hexTc.SetValue(returnHex.lstrip('#').upper())
        self.mainPanel.SetBackgroundColour(returnHex)
        self.Refresh()

    def onCopyRGB(self, event):
        textToCopy = 'rgb('+self.rTc.GetValue()+', '+self.gTc.GetValue()+', '+self.bTc.GetValue()+')'
        pc.copy(textToCopy)

    def onCopyHex(self, event):
        textToCopy = '#'+self.hexTc.GetValue().upper()
        pc.copy(textToCopy)

if __name__ == '__main__':
    app = wx.App()
    App()
    app.MainLoop()

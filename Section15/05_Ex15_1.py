class Computer:
    def set_spec(self,cpu,ram,vga,ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('ram = {}'.format(self.ram))
        print('vga = {}'.format(self.vga))
        print('ssd = {}'.format(self.ssd))

desktop = Computer()
desktop.set_spec('i7','16GB','GTX1060','512GB')
desktop.hardware_info()

notebook = Computer()
notebook.set_spec('i5','8GB','MX300','256GB')
notebook.hardware_info()
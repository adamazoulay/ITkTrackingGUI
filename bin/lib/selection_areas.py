class BoardItem:
    def __init__(self, name, description, signal, direction, pad_type, coords, comments):
        self.name = name
        self.description = description
        self.signal = signal
        self.direction = direction
        self.pad_type = pad_type
        self.coords = coords
        self.comments = comments


# Same for all ASICS
ASIC = {
    'BP1': BoardItem('XOFFRB', 'Data signal (bidirectional)', '160', 'I/O', 'SLVS',
                     [(1689.1, 1363.9), (1703.9, 1363.9), (1703.9, 1397.5), (1689.1, 1397.5)], ''),
    'BP2': BoardItem('XOFFR', 'Data signal (bidirectional)', '160', 'I/O', 'SLVS',
                     [(1653.4, 1363.9), (1668.2, 1363.9), (1668.2, 1397.5), (1653.4, 1397.5)], ''),
    'BP3': BoardItem('GNDD', 'Digital  Ground', '0V', 'POWER', 'Digital Ground',
                     [(1630.0, 1360.9), (1644.8, 1360.9), (1644.8, 1394.5), (1630.0, 1394.5)], ''),
    'BP4': BoardItem('DATRB', 'Data signal (bidirectional)', '160', 'I/O', 'SLVS',
                     [(1610.6, 1360.9), (1625.4, 1360.9), (1625.4, 1394.5), (1610.6, 1394.5)], ''),
    'BP5': BoardItem('DATR', 'Data signal (bidirectional)', '160', 'I/O', 'SLVS',
                     [(1571.8, 1363.9), (1586.6, 1363.9), (1586.6, 1397.5), (1571.8, 1397.5)], ''),
    'BP6': BoardItem('DVSS', '0V Ground Specific for ESD Return', '0V', 'POWER', 'ESD Return',
                     [(1553.5, 1363.9), (1568.3, 1363.9), (1568.3, 1397.5), (1553.5, 1397.5)], ''),
    'BP7': BoardItem('dataOutFC2_padN', 'Fast ClusterFinder data output', '320/640', 'O', 'SLVS',
                     [(1473.9, 1362.9), (1488.7, 1362.9), (1488.7, 1396.5), (1473.9, 1396.5)], ''),
    'BP8': BoardItem('dataOutFC2_padP', 'Fast ClusterFinder data output', '320/640', 'O', 'SLVS',
                     [(1394.4, 1363.9), (1409.2, 1363.9), (1409.2, 1397.5), (1394.4, 1397.5)], ''),
    'BP9': BoardItem('DVSS', '0V Ground Specific for ESD Return', '0V', 'POWER', 'ESD Return',
                     [(1375.0, 1363.9), (1389.8, 1363.9), (1389.8, 1397.5), (1375.0, 1397.5)], ''),
    'BP10': BoardItem('dataOutFC1_padN', 'Fast ClusterFinder data output', '320/640', 'O', 'SLVS',
                      [(1353.6, 1365.0), (1368.4, 1365.0), (1368.4, 1398.6), (1353.6, 1398.6)], ''),
    'BP11': BoardItem('dataOutFC1_padP', 'Fast ClusterFinder data output', '320/640', 'O', 'SLVS',
                      [(1333.2, 1365.0), (1348.0, 1365.0), (1348.0, 1398.6), (1333.2, 1398.6)], ''),
    'BP12': BoardItem('DVDD', 'External Power for Digital', '1.5V', 'POWER', 'Ext. Digital Power',
                      [(1313.8, 1367.0), (1328.6, 1367.0), (1328.6, 1400.6), (1313.8, 1400.6)], ''),
    'BP13': BoardItem('VDDD', 'Regulated Power for Digital', '1.2V', 'POWER', 'Reg. Digital Power',
                      [(1292.4, 1366.0), (1307.2, 1366.0), (1307.2, 1399.6), (1292.4, 1399.6)], ''),
    'BP14': BoardItem('GNDD', 'Digital  Ground', '0V', 'POWER', 'Digital Ground',
                      [(1272.0, 1366.0), (1286.8, 1366.0), (1286.8, 1399.6), (1272.0, 1399.6)], ''),
    'BP15': BoardItem('DVDD', 'External Power for Digital', '1.5V', 'POWER', 'Ext. Digital Power',
                      [(1250.6, 1365.0), (1265.4, 1365.0), (1265.4, 1398.6), (1250.6, 1398.6)], ''),
    'BP16': BoardItem('VDDD', 'Regulated Power for Digital', '1.2V', 'POWER', 'Reg. Digial Power',
                      [(1230.2, 1368.0), (1245.0, 1368.0), (1245.0, 1401.6), (1230.2, 1401.6)], ''),
    'BP17': BoardItem('GNDD', 'Digital  Ground', '0V', 'POWER', 'Digital Ground',
                      [(1206.7, 1366.0), (1221.5, 1366.0), (1221.5, 1399.6), (1206.7, 1399.6)], ''),
    'BP18': BoardItem('DVDD', 'External Power for Digital', '1.5V', 'POWER', 'Ext. Digital Power',
                      [(1185.3, 1367.0), (1200.1, 1367.0), (1200.1, 1400.6), (1185.3, 1400.6)], ''),
    'BP19': BoardItem('VDDD', 'Regulated Power for Digital', '1.2V', 'POWER', 'Reg. Digital Power',
                      [(1165.9, 1367.0), (1180.7, 1367.0), (1180.7, 1400.6), (1165.9, 1400.6)], ''),
    'BP20': BoardItem('GNDD', 'Digital  Ground', '0V', 'POWER', 'Digital Ground',
                      [(1143.5, 1367.0), (1158.3, 1367.0), (1158.3, 1400.6), (1143.5, 1400.6)], ''),
    'BP21': BoardItem('', '', '', '', '', [(1124.1, 1367.0), (1138.9, 1367.0), (1138.9, 1400.6), (1124.1, 1400.6)], ''),
    'BP22': BoardItem('DVSSA', '0V Ground Specific for ESD Return', '0V', 'POWER', 'ESD Return',
                      [(1103.7, 1367.0), (1118.5, 1367.0), (1118.5, 1400.6), (1103.7, 1400.6)], ''),
    'BP23': BoardItem('AVDD', 'External Power for Analog', '1.5V', 'POWER', 'Ext. Analog Power',
                      [(1082.3, 1366.0), (1097.1, 1366.0), (1097.1, 1399.6), (1082.3, 1399.6)], ''),
    'BP24': BoardItem('GNDA', 'Analog Ground', '0V', 'POWER', 'Analog Ground',
                      [(1061.9, 1367.0), (1076.7, 1367.0), (1076.7, 1400.6), (1061.9, 1400.6)], ''),
    'BP25': BoardItem('VDDA', 'Regulated Power for Analog', '1.2V', 'POWER', 'Reg. Analog Power',
                      [(1040.5, 1368.0), (1055.3, 1368.0), (1055.3, 1401.6), (1040.5, 1401.6)], ''),
    'BP26': BoardItem('GNDIt', '0V Analog Ground to ESD Branch', '0V', 'POWER', 'Analog Ground',
                      [(1020.1, 1366.0), (1034.9, 1366.0), (1034.9, 1399.6), (1020.1, 1399.6)], ''),
    'BP27': BoardItem('AVDD', 'External Power for Analog', '1.5V', 'POWER', 'Ext. Analog Power',
                      [(1000.7, 1366.0), (1015.5, 1366.0), (1015.5, 1399.6), (1000.7, 1399.6)], ''),
    'BP28': BoardItem('GNDA', 'Analog Ground', '0V', 'POWER', 'Analog Ground',
                      [(978.3, 1367.0), (993.1, 1367.0), (993.1, 1400.6), (978.3, 1400.6)], ''),
    'BP29': BoardItem('VDDA', 'Regulated Power for Analog', '1.2V', 'POWER', 'Reg. Analog Power',
                      [(956.9, 1367.0), (971.7, 1367.0), (971.7, 1400.6), (956.9, 1400.6)], ''),
    'BP30': BoardItem('GNDIt', '0V analogue Ground to FE branch', '0V', 'POWER', 'Analog Ground',
                      [(937.5, 1367.0), (952.3, 1367.0), (952.3, 1400.6), (937.5, 1400.6)], ''),
    'BP31': BoardItem('AVDD', 'External Power for Analog', '1.5V', 'POWER', 'Ext. Analog Power',
                      [(916.1, 1368.0), (930.9, 1368.0), (930.9, 1401.6), (916.1, 1401.6)], ''),
    'BP32': BoardItem('GNDA', 'Analog Ground', '0V', 'POWER', 'Analog Ground',
                      [(895.7, 1368.0), (910.5, 1368.0), (910.5, 1401.6), (895.7, 1401.6)], ''),
    'BP33': BoardItem('VDDA', 'Regulated Power for Analog', '1.2V', 'POWER', 'Reg. Analog Power',
                      [(873.2, 1368.0), (888.0, 1368.0), (888.0, 1401.6), (873.2, 1401.6)], ''),
    'BP34': BoardItem('GNDIt', '0V analogue Ground to FE branch', '0V', 'POWER', 'Analog Ground',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP35': BoardItem('AVDD', 'External Power for Analog', '1.5V', 'POWER', 'Ext. Analog Power',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP36': BoardItem('GNDA', 'Analog Ground', '0V', 'POWER', 'Analog Ground', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP37': BoardItem('VDDA', 'Regulated Power for Analog', '1.2V', 'POWER', 'Reg. Analog Power',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP38': BoardItem('GNDIT', '0V analogue Ground to FE branch', '0V', 'POWER', 'Analog Ground',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP39': BoardItem('DVSSA', '0V Ground Specific for ESD Return', '0V', 'POWER', 'ESD Return',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP40': BoardItem('DVSS', '0V Ground Specific for ESD Return', '0V', 'POWER', 'ESD Return',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP41': BoardItem('VDDD', 'Regulated Power for Digital', '1.2V', 'POWER', 'Reg. Digial Power',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP42': BoardItem('DVDD', 'External Power for Digital', '1.5V', 'POWER', 'Ext. Digital Power',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP43': BoardItem('GNDD', 'Digital  Ground', '0V', 'POWER', 'Digital Ground', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP44': BoardItem('VDDD', 'Regulated Power for Digital', '1.2V', 'POWER', 'Reg. Digial Power',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP45': BoardItem('DVDD', 'External Power for Digital', '1.5V', 'POWER', 'Ext. Digital Power',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP46': BoardItem('GNDD', 'Digital  Ground', '0V', 'POWER', 'Digital Ground', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP47': BoardItem('padID<4>', 'Chip Address', 'Static', 'I', 'CMOS Pull-down', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP48': BoardItem('padID<3>', 'Chip Address', 'Static', 'I', 'CMOS Pull-down', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP49': BoardItem('padID<2>', 'Chip Address', 'Static', 'I', 'CMOS Pull-down', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP50': BoardItem('padID<1>', 'Chip Address', 'Static', 'I', 'CMOS Pull-down', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP51': BoardItem('padID<0>', 'Chip Address', 'Static', 'I', 'CMOS Pull-down', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP52': BoardItem('padTerm', 'SLVS Termination On/Off', 'Static', 'I', 'CMOS Pull-up',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP53': BoardItem('FastCLK_padP', 'Fast ClusterFinder clock input', '320/640', 'I', 'SLVS',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP54': BoardItem('FastCLK_padN', 'Fast ClusterFinder clock input', '320/640', 'I', 'SLVS',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP55': BoardItem('GNDD', 'Digital  Ground', '0V', 'POWER', 'Digital Ground', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP56': BoardItem('DATL', 'Data signal (bidirectional)', '160', 'I/O', 'SLVS', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP57': BoardItem('DATLB', 'Data signal (bidirectional)', '160', 'I/O', 'SLVS', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP58': BoardItem('DVSS', '0V Ground Specific for ESD Return', '0V', 'POWER', 'ESD Return',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP59': BoardItem('XOFFL', 'XDFF signal (bidirectional)', '160', 'I/O', 'SLVS', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP60': BoardItem('XOFFLB', 'XDFF signal (bidirectional)', '160', 'I/O', 'SLVS', [(0, 0), (0, 0), (0, 0), (0, 0)],
                      ''),
    'BP61': BoardItem('Pad_Label_Not_Found', 'Fiducial', '', '', '', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP62': BoardItem('padShuntCtrl', 'Shunt Device Control (analogue signal)', 'Analogue', 'I', 'Analogue',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP63': BoardItem('padDisable_RegD', 'Disable Regulator (Digital)', 'Static', 'I', 'CMOS Pull-Down',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP64': BoardItem('padDisable_RegA', 'Disable Regulator (Analogue)', 'Static', 'I', 'CMOS Pull-Down',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP65': BoardItem('Pad_Label_Not_Found', '', '', '', '', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP66': BoardItem('LONERTHREE_padP', 'Multiplexed R3 L1 input (80mb/s)', '80', 'I', 'SLVS',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP67': BoardItem('LONERTHREE_padN', 'Multiplexed R3 L1 input (80mb/s)', '80', 'I', 'SLVS',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP68': BoardItem('GNDx', '', '', '', '', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP69': BoardItem('COM_LZERO_padP', 'Multiplexed Com L0 input (80mb/s)', '80', 'I', 'SLVS',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP70': BoardItem('COM_LZERO_padN', 'Multiplexed Com L0 input (80mb/s)', '80', 'I', 'SLVS',
                      [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP71': BoardItem('GNDx', '', '', '', '', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP72': BoardItem('CLK_padP', 'Readout Rate clock input', '40', 'I', 'SLVS', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP73': BoardItem('CLK_padN', 'Readout Rate clock input', '40', 'I', 'SLVS', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP74': BoardItem('GNDx', '', '', '', '', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP75': BoardItem('Pad_Label_Not_Found', 'Fiducial', '', '', '', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP76': BoardItem('BC_padP', '40 Mhz clock input', '160', 'I', 'SLVS', [(0, 0), (0, 0), (0, 0), (0, 0)], ''),
    'BP77': BoardItem('BC_padN', '40 Mhz clock input', '160', 'I', 'SLVS', [(0, 0), (0, 0), (0, 0), (0, 0)], '')}

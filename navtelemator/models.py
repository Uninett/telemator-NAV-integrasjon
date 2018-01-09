# coding: utf-8
from sqlalchemy import Column, DateTime, Index, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from django.core.urlresolvers import reverse


Base = declarative_base()
metadata = Base.metadata

# Classes actually used


class Cable(Base):
    __tablename__ = 'KabReg'

    RowKey = Column(Integer, primary_key=True)
    Cable = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    CoreType = Column(Numeric(2, 0))
    NumCores = Column(Numeric(5, 0))
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'), ForeignKey('ElmOwner.Owner'))
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Usage = Column(String(12, 'Danish_Norwegian_CI_AS'))
    End_A = Column(String(30, 'Danish_Norwegian_CI_AS'), ForeignKey('EndReg.End'), index=True)
    End_B = Column(String(30, 'Danish_Norwegian_CI_AS'), ForeignKey('EndReg.End'), index=True)
    Length = Column(Numeric(8, 0))
    DtPlaced = Column(DateTime)
    Coverage = Column(String(8, 'Danish_Norwegian_CI_AS'))
    TypeCode = Column(String(30, 'Danish_Norwegian_CI_AS'))
    ColorCode = Column(String(25, 'Danish_Norwegian_CI_AS'))
    AutRoutBlk = Column(Numeric(1, 0))
    Broken = Column(Numeric(1, 0))
    RedundGrp = Column(Numeric(10, 0))
    Speed = Column(String(10, 'Danish_Norwegian_CI_AS'))
    ServiceLvl = Column(String(1, 'Danish_Norwegian_CI_AS'))
    Product = Column(String(12, 'Danish_Norwegian_CI_AS'))
    TslStruc = Column(String(20, 'Danish_Norwegian_CI_AS'))
    ForPerCost = Column(Numeric(10, 2))
    Currency = Column(String(3, 'Danish_Norwegian_CI_AS'))
    EtabCost = Column(Numeric(7, 0))
    DtEtabCost = Column(DateTime)
    EtabCost2 = Column(Numeric(7, 0))
    DtEtabCos2 = Column(DateTime)
    ServiCost = Column(Numeric(10, 2))
    DtServiCos = Column(DateTime)
    InvPeriod = Column(Numeric(2, 0))
    PeriodCost = Column(Numeric(10, 2))
    DtPeriodCo = Column(DateTime)
    BindTo = Column(DateTime)
    AgrDurMth = Column(String(2, 'Danish_Norwegian_CI_AS'))
    TermOfNoti = Column(Numeric(2, 0))
    RenewTerm = Column(String(10, 'Danish_Norwegian_CI_AS'))
    SentRequ = Column(DateTime)
    PlanDeliv = Column(DateTime)
    OffRecv = Column(DateTime)
    OffDeliv = Column(DateTime)
    Ordered = Column(DateTime)
    OrdDeliv = Column(DateTime)
    AcknRecvd = Column(DateTime)
    AcknDeliv = Column(DateTime)
    InUse = Column(DateTime)
    RcvTeFiMsg = Column(DateTime)
    RcvTeFiEst = Column(DateTime)
    CancldFrom = Column(DateTime)
    CancldUpdU = Column(String(20, 'Danish_Norwegian_CI_AS'))
    CancldCode = Column(String(2, 'Danish_Norwegian_CI_AS'))
    LastDebit = Column(DateTime)
    TakenDown = Column(DateTime)
    PaidUntil = Column(DateTime)
    FwdInvTo = Column(String(10, 'Danish_Norwegian_CI_AS'))
    PriceAdj1 = Column(Numeric(9, 2))
    DtPriceAd1 = Column(DateTime)
    PriceAdj2 = Column(Numeric(9, 2))
    Discount = Column(Numeric(5, 2))
    Account = Column(String(4, 'Danish_Norwegian_CI_AS'))
    CostCenter = Column(String(10, 'Danish_Norwegian_CI_AS'))
    CostProj = Column(String(7, 'Danish_Norwegian_CI_AS'))
    Reference = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Status = Column(String(10, 'Danish_Norwegian_CI_AS'))
    CustId = Column(String(18, 'Danish_Norwegian_CI_AS'), index=True)
    NumItems = Column(Numeric(5, 0))
    AgreemId = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    ExtSysTxt = Column(String(30, 'Danish_Norwegian_CI_AS'))
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))
    InstVendor = Column(String(30, 'Danish_Norwegian_CI_AS'))
    SaInvAmoun = Column(Numeric(7, 0))
    SaRdyToInv = Column(DateTime)
    SaSentInv = Column(DateTime)
    SaInvRef = Column(String(20, 'Danish_Norwegian_CI_AS'))
    SaDlvCoord = Column(String(30, 'Danish_Norwegian_CI_AS'))

    end_a = relationship('End', foreign_keys=[End_A])
    end_b = relationship('End', foreign_keys=[End_B])
    owner = relationship('Owner', back_populates='cables')
    routingcables = relationship('RoutingCable', back_populates='cable')

    def get_absolute_url(self):
        return reverse('cable-info', args=[str(self.Cable)])

    def reference(self):
        return str(self.End_A) + '-' + str(self.End_B)


class Circuit(Base):
    __tablename__ = 'SbReg'

    RowKey = Column(Integer, primary_key=True)
    Circuit = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    RelateType = Column(String(1, 'Danish_Norwegian_CI_AS'))
    Type = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'), ForeignKey('ElmOwner.Owner'))
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Speed = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Wavelength = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Attenuat = Column(Numeric(4, 1))
    Reference = Column(String(25, 'Danish_Norwegian_CI_AS'))
    CircGrpId = Column(Numeric(10, 0))
    NumWires = Column(Numeric(2, 0))
    Category = Column(String(12, 'Danish_Norwegian_CI_AS'))
    DtOrdered = Column(DateTime)
    DtOrdDeliv = Column(DateTime)
    DtRdyToUse = Column(DateTime)
    DtTakeDown = Column(DateTime)
    DtShutDown = Column(DateTime)
    PeriodCost = Column(Numeric(10, 2))
    Signaling = Column(String(10, 'Danish_Norwegian_CI_AS'))
    ServiceLvl = Column(String(1, 'Danish_Norwegian_CI_AS'))
    MailNotOff = Column(Numeric(1, 0))
    Engineer = Column(String(30, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    ExtSysTxt = Column(String(30, 'Danish_Norwegian_CI_AS'))
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))

    customers = relationship('CustomerCircuit', back_populates='circuit')
    owner = relationship('Owner', back_populates='circuits')
    routingcables = relationship('RoutingCable', back_populates='circuit')
    connections = relationship('Connection', back_populates='circuit')


    def get_absolute_url(self):
        return reverse('circuit-info', args=[str(self.Circuit)])


class CircuitEnd(Base):
    __tablename__ = 'UtsTlf'
    __table_args__ = (
        Index('TM_0122', 'Circuit', 'Parallel', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    Circuit = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Parallel = Column(Integer, nullable=False)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    Phone = Column(String(20, 'Danish_Norwegian_CI_AS'))
    dBmTx = Column(Numeric(6, 2))
    dBmRx = Column(Numeric(6, 2))
    dBmWhen = Column(DateTime)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class Connection(Base):
    __tablename__ = 'UtsTilk'
    __table_args__ = (
        Index('TM_0136', 'End', 'Card', 'Port', 'Pin', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), ForeignKey('EndReg.End'), nullable=False)
    Card = Column(String(22, 'Danish_Norwegian_CI_AS'), nullable=False)
    Port = Column(Numeric(4, 0), nullable=False)
    Pin = Column(Numeric(2, 0), nullable=False)
    Signal = Column(String(8, 'Danish_Norwegian_CI_AS'))
    Cable = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    Core = Column(Integer)
    Circuit = Column(String(30, 'Danish_Norwegian_CI_AS'), ForeignKey('SbReg.Circuit'), index=True)
    Wire = Column(String(1, 'Danish_Norwegian_CI_AS'))
    Xinfo = Column(String(10, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))

    circuit = relationship('Circuit', back_populates='connections')
    end = relationship('End', back_populates='connections')


class Customer(Base):
    __tablename__ = 'AboReg'

    RowKey = Column(Integer, primary_key=True)
    CustId = Column(String(18, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    Name = Column(String(40, 'Danish_Norwegian_CI_AS'))
    OrgNum = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Function = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Department = Column(String(45, 'Danish_Norwegian_CI_AS'))
    Addr2 = Column(String(45, 'Danish_Norwegian_CI_AS'))
    Addr3 = Column(String(45, 'Danish_Norwegian_CI_AS'))
    MobPhone = Column(String(11, 'Danish_Norwegian_CI_AS'))
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    ExtSysTxt = Column(String(30, 'Danish_Norwegian_CI_AS'))
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))

    circuits = relationship('CustomerCircuit', back_populates='customer', order_by='Circuit.Circuit')

    def get_absolute_url(self):
        return reverse('customer-info', args=[str(self.CustId)])


class CustomerCircuit(Base):
    __tablename__ = 'KuSbLink'
    __table_args__ = (
        Index('TM_0120', 'CustId', 'Circuit', 'Parallel', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    CustId = Column(String(18, 'Danish_Norwegian_CI_AS'), ForeignKey('AboReg.CustId'), nullable=False)
    Circuit = Column(String(30, 'Danish_Norwegian_CI_AS'), ForeignKey('SbReg.Circuit'), nullable=False, index=True)
    Parallel = Column(Integer, nullable=False)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))

    customer = relationship('Customer', back_populates='circuits')
    circuit = relationship('Circuit', back_populates='customers')


class End(Base):
    __tablename__ = 'EndReg'

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    EqLinkToPt = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    IsEquipm = Column(Numeric(1, 0), nullable=False)
    Type = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Addr1 = Column(String(45, 'Danish_Norwegian_CI_AS'))
    Addr2 = Column(String(45, 'Danish_Norwegian_CI_AS'))
    Addr3 = Column(String(45, 'Danish_Norwegian_CI_AS'))
    Cadastre = Column(String(25, 'Danish_Norwegian_CI_AS'))
    Usage = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Drawing = Column(String(25, 'Danish_Norwegian_CI_AS'))
    Manufact = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Material = Column(String(15, 'Danish_Norwegian_CI_AS'))
    NumMater = Column(Numeric(3, 0))
    Latitude = Column(Numeric(15, 6))
    Longitude = Column(Numeric(15, 6))
    UTMzone = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Elevation = Column(Numeric(4, 0))
    Height = Column(Numeric(4, 0))
    SerialNo = Column(String(25, 'Danish_Norwegian_CI_AS'))
    ServiceLvl = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Status = Column(String(10, 'Danish_Norwegian_CI_AS'))
    TrmTxtHint = Column(Numeric(2, 0))
    Rack = Column(String(30, 'Danish_Norwegian_CI_AS'))
    PosInRack = Column(String(6, 'Danish_Norwegian_CI_AS'))
    HeigInRack = Column(Numeric(3, 0))
    BindTo = Column(DateTime)
    InvPeriod = Column(Numeric(2, 0))
    Currency = Column(String(3, 'Danish_Norwegian_CI_AS'))
    EtabCost = Column(Numeric(7, 0))
    PeriodCost = Column(Numeric(10, 2))
    PriceAdj1 = Column(Numeric(9, 2))
    PriceAdj2 = Column(Numeric(9, 2))
    Discount = Column(Numeric(2, 0))
    Account = Column(String(4, 'Danish_Norwegian_CI_AS'))
    CostCenter = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Reference = Column(String(20, 'Danish_Norwegian_CI_AS'))
    PaidUntil = Column(DateTime)
    FwdInvTo = Column(String(10, 'Danish_Norwegian_CI_AS'))
    AcknDeliv = Column(DateTime)
    InUse = Column(DateTime)
    CancldFrom = Column(DateTime)
    TakenDown = Column(DateTime)
    ElYearkWh = Column(Numeric(8, 0))
    ElNeVendor = Column(String(30, 'Danish_Norwegian_CI_AS'))
    ElNeMeter = Column(Numeric(8, 0))
    ElNeMetId = Column(String(34, 'Danish_Norwegian_CI_AS'))
    ElNeMePtId = Column(Numeric(8, 0))
    ElNeInvo = Column(String(8, 'Danish_Norwegian_CI_AS'))
    ElNePaidDt = Column(DateTime)
    ElEnVendor = Column(String(30, 'Danish_Norwegian_CI_AS'))
    ElEnInvo = Column(String(8, 'Danish_Norwegian_CI_AS'))
    ElEnPaidDt = Column(DateTime)
    ElCoVendor = Column(String(30, 'Danish_Norwegian_CI_AS'))
    ElCoMeter = Column(Numeric(8, 0))
    ElCoMetId = Column(String(34, 'Danish_Norwegian_CI_AS'))
    ElCoMePtId = Column(Numeric(8, 0))
    ElCoInvo = Column(String(8, 'Danish_Norwegian_CI_AS'))
    ElCoPaidDt = Column(DateTime)
    PosFibVend = Column(String(30, 'Danish_Norwegian_CI_AS'))
    AreaIndo = Column(Numeric(4, 0))
    AreaOutd = Column(Numeric(4, 0))
    CustId = Column(String(18, 'Danish_Norwegian_CI_AS'), index=True)
    InveNumb = Column(String(15, 'Danish_Norwegian_CI_AS'))
    InveOthLbl = Column(String(50, 'Danish_Norwegian_CI_AS'))
    InveIsLbld = Column(Numeric(1, 0))
    InveDtLtst = Column(DateTime)
    SNMPcommun = Column(String(20, 'Danish_Norwegian_CI_AS'))
    CoolerkW = Column(Numeric(5, 1))
    AuthClass = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Extra1 = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Extra2 = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Extra3 = Column(String(20, 'Danish_Norwegian_CI_AS'))
    AuRoStepOk = Column(Numeric(1, 0))
    DelLocked = Column(Numeric(1, 0))
    UpdLocked = Column(Numeric(1, 0))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    ExtSysTxt = Column(String(30, 'Danish_Norwegian_CI_AS'))
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))
    AccToSiteM = Column(String(collation='Danish_Norwegian_CI_AS'))
    MapRef = Column(String(1, 'Danish_Norwegian_CI_AS'))

    ports = relationship('Port', back_populates='end')
    connections = relationship('Connection', back_populates='end')

    def get_absolute_url(self):
        if self.IsEquipm == 1:
            if self.Type == 'CWDM':
                return reverse('telemator-netbox-info', args=[str(self.End)])
            return reverse('ipdevinfo-details-by-name', args=[str(self.End.lower())])
        return reverse('room-info', args=[str(self.End.lower())])


class Owner(Base):
    __tablename__ = 'ElmOwner'

    RowKey = Column(Integer, primary_key=True)
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    Name = Column(String(254, 'Danish_Norwegian_CI_AS'))
    Type = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Email = Column(String(50, 'Danish_Norwegian_CI_AS'))
    Email2 = Column(String(50, 'Danish_Norwegian_CI_AS'))
    Phone = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Phone2 = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Contact = Column(String(25, 'Danish_Norwegian_CI_AS'))
    Contact2 = Column(String(25, 'Danish_Norwegian_CI_AS'))
    Remark = Column(String(50, 'Danish_Norwegian_CI_AS'))
    Whitelist = Column(String(90, 'Danish_Norwegian_CI_AS'))
    Blacklist = Column(String(90, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))

    circuits = relationship('Circuit', back_populates='owner', order_by='Circuit.Circuit')
    cables = relationship('Cable', back_populates='owner', order_by='Cable.Cable')

    def get_absolute_url(self):
        return reverse('owner-info', args=[str(self.Owner)])


class Port(Base):
    __tablename__ = 'UtsUtg'
    __table_args__ = (
        Index('TM_0135', 'End', 'Card', 'Port', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), ForeignKey('EndReg.End'), nullable=False)
    Card = Column(String(22, 'Danish_Norwegian_CI_AS'), nullable=False)
    Port = Column(Numeric(4, 0), nullable=False)
    Label = Column(String(254, 'Danish_Norwegian_CI_AS'))
    Type = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Setting = Column(String(20, 'Danish_Norwegian_CI_AS'))
    NumPins = Column(Numeric(2, 0))
    Channel = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Reserved = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Remark = Column(String(254, 'Danish_Norwegian_CI_AS'))
    IsHidePort = Column(Numeric(1, 0))
    IsRoutBlk = Column(Numeric(1, 0))
    LineSide = Column(Numeric(1, 0))
    Wireless = Column(Numeric(1, 0))
    TR_Card = Column(String(22, 'Danish_Norwegian_CI_AS'))
    TR_Port = Column(Numeric(4, 0))
    XinfoInt = Column(String(5, 'Danish_Norwegian_CI_AS'))
    AN_CabTp = Column(String(20, 'Danish_Norwegian_CI_AS'))
    AN_CabLen = Column(Numeric(8, 0))
    AN_Type = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Gain_dB = Column(String(7, 'Danish_Norwegian_CI_AS'))
    AN_Polar = Column(String(10, 'Danish_Norwegian_CI_AS'))
    AN_Altitud = Column(String(7, 'Danish_Norwegian_CI_AS'))
    AN_Heigh = Column(String(7, 'Danish_Norwegian_CI_AS'))
    AN_Diam = Column(String(7, 'Danish_Norwegian_CI_AS'))
    AN_Direc = Column(String(10, 'Danish_Norwegian_CI_AS'))
    TX_MHz = Column(String(9, 'Danish_Norwegian_CI_AS'))
    RX_MHz = Column(String(9, 'Danish_Norwegian_CI_AS'))
    ChWidthMHz = Column(String(7, 'Danish_Norwegian_CI_AS'))
    TX_out_dBm = Column(String(7, 'Danish_Norwegian_CI_AS'))
    RX_in_dBm = Column(String(7, 'Danish_Norwegian_CI_AS'))
    AGC_Volt = Column(String(7, 'Danish_Norwegian_CI_AS'))
    Modulation = Column(String(7, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))

    end = relationship('End', back_populates='ports')


class RoutingCable(Base):
    __tablename__ = 'LedRut'
    __table_args__ = (
        Index('TM_0108', 'Cable', 'Core', unique=True),
        Index('TM_0110', 'TrunkCable', 'TrunkCore')
    )

    RowKey = Column(Integer, primary_key=True)
    Cable = Column(String(30, 'Danish_Norwegian_CI_AS'), ForeignKey('KabReg.Cable'), nullable=False)
    Core = Column(Integer, nullable=False)
    Circuit = Column(String(30, 'Danish_Norwegian_CI_AS'), ForeignKey('SbReg.Circuit'), index=True)
    Wire = Column(String(1, 'Danish_Norwegian_CI_AS'))
    Xinfo_A = Column(String(6, 'Danish_Norwegian_CI_AS'))
    Xinfo_B = Column(String(6, 'Danish_Norwegian_CI_AS'))
    DtRouted = Column(DateTime)
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'))
    FaultCode = Column(String(2, 'Danish_Norwegian_CI_AS'))
    Remark = Column(String(40, 'Danish_Norwegian_CI_AS'))
    Reserved = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Att1310 = Column(Numeric(5, 2))
    Att1550 = Column(Numeric(5, 2))
    Att1625 = Column(Numeric(5, 2))
    TrunkCable = Column(String(30, 'Danish_Norwegian_CI_AS'))
    TrunkCore = Column(Integer)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))

    cable = relationship('Cable', back_populates='routingcables')
    circuit = relationship('Circuit', back_populates='routingcables')


# Classes not currently used


class CircServ(Base):
    __tablename__ = 'CircServ'
    __table_args__ = (
        Index('TM_0118', 'Circuit', 'Service', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    Circuit = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Service = Column(String(12, 'Danish_Norwegian_CI_AS'), nullable=False)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class ElmAlia(Base):
    __tablename__ = 'ElmAlias'
    __table_args__ = (
        Index('TM_0127', 'RelToTbl', 'RelToKey', 'AliasTxt', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    RelToTbl = Column(String(1, 'Danish_Norwegian_CI_AS'), nullable=False)
    RelToKey = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    AliasTxt = Column(String(64, 'Danish_Norwegian_CI_AS'), nullable=False)
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Remark = Column(String(40, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class EndPower(Base):
    __tablename__ = 'EndPower'
    __table_args__ = (
        Index('TM_0130', 'End', 'PowerCirc', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    PowerCirc = Column(String(12, 'Danish_Norwegian_CI_AS'))
    Voltage = Column(String(6, 'Danish_Norwegian_CI_AS'))
    ThreePhase = Column(Numeric(1, 0))
    FuseAmp = Column(Numeric(4, 0))
    LeasedWatt = Column(Numeric(5, 0))
    DtInstalld = Column(DateTime)
    Vendor = Column(String(30, 'Danish_Norwegian_CI_AS'))
    State = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Remark = Column(String(60, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class EndRack(Base):
    __tablename__ = 'EndRack'
    __table_args__ = (
        Index('TM_0128', 'End', 'Rack', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Rack = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Type = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Height = Column(Numeric(4, 0))
    Width = Column(Numeric(4, 0))
    Depth = Column(Numeric(4, 0))
    PosTopmost = Column(Numeric(4, 0))
    PosBottom = Column(Numeric(4, 0))
    PosUnit = Column(Numeric(1, 0))
    PosUnavail = Column(String(50, 'Danish_Norwegian_CI_AS'))
    CustId = Column(String(18, 'Danish_Norwegian_CI_AS'), index=True)
    PowerCirc = Column(String(148, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))


class EndServ(Base):
    __tablename__ = 'EndServ'
    __table_args__ = (
        Index('TM_0117', 'End', 'Service', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Service = Column(String(12, 'Danish_Norwegian_CI_AS'), nullable=False)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class Engineer(Base):
    __tablename__ = 'Engineer'

    RowKey = Column(Integer, primary_key=True)
    Engineer = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    Name = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Department = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Phone = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Email = Column(String(50, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class EqTrunk(Base):
    __tablename__ = 'EqTrunk'

    RowKey = Column(Integer, primary_key=True)
    TrunkEq = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    Function = Column(Numeric(1, 0), nullable=False)
    Type = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    InUse = Column(DateTime)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))


class EqVlan(Base):
    __tablename__ = 'EqVlan'

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Card = Column(String(22, 'Danish_Norwegian_CI_AS'), nullable=False)
    Port = Column(Numeric(4, 0), nullable=False)
    Vlan = Column(String(20, 'Danish_Norwegian_CI_AS'), nullable=False)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class ExtLink(Base):
    __tablename__ = 'ExtLinks'

    RowKey = Column(Integer, primary_key=True)
    RelToTbl = Column(String(1, 'Danish_Norwegian_CI_AS'), nullable=False, index=True)
    RelToKey = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    Name = Column(String(60, 'Danish_Norwegian_CI_AS'))
    Target = Column(String(254, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class Invoice(Base):
    __tablename__ = 'Invoice'

    RowKey = Column(Integer, primary_key=True)
    Vendor = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Invoice = Column(String(15, 'Danish_Norwegian_CI_AS'), nullable=False)
    RelToTbl = Column(String(1, 'Danish_Norwegian_CI_AS'), nullable=False, index=True)
    RelToKey = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, index=True)
    DtInvoice = Column(DateTime)
    Amount = Column(Numeric(10, 2))
    Remark = Column(String(40, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class KabTer(Base):
    __tablename__ = 'KabTer'
    __table_args__ = (
        Index('TM_0104', 'Cable', 'IsEnd_A', 'FromCore', 'IsDraft', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    Cable = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    FromCore = Column(Integer, nullable=False)
    IsEnd_A = Column(Numeric(1, 0), nullable=False)
    IsDraft = Column(Numeric(1, 0), nullable=False)
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    TrmTxt = Column(Numeric(2, 0), nullable=False)
    NumCores = Column(Integer)
    PosPrPli = Column(Numeric(4, 0))
    PinPrPos = Column(Numeric(2, 0))
    Rack = Column(String(30, 'Danish_Norwegian_CI_AS'))
    PosInRack = Column(String(6, 'Danish_Norwegian_CI_AS'))
    HeigInRack = Column(Numeric(3, 0))
    Plinth = Column(String(25, 'Danish_Norwegian_CI_AS'))
    Pos = Column(String(6, 'Danish_Norwegian_CI_AS'))
    Pin = Column(Numeric(2, 0))
    PosZerBas = Column(Numeric(1, 0))
    PliDir = Column(String(20, 'Danish_Norwegian_CI_AS'))
    PliType = Column(String(20, 'Danish_Norwegian_CI_AS'))
    PosType = Column(String(25, 'Danish_Norwegian_CI_AS'))
    DtSpliced = Column(DateTime)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class KabToDo(Base):
    __tablename__ = 'KabToDo'

    RowKey = Column(Integer, primary_key=True)
    TodoId = Column(Numeric(6, 0), nullable=False)
    RelToTbl = Column(String(1, 'Danish_Norwegian_CI_AS'), nullable=False, index=True)
    RelToKey = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    PlannedDt = Column(DateTime)
    ActDate = Column(DateTime)
    ActType = Column(String(5, 'Danish_Norwegian_CI_AS'))
    OnHold = Column(Numeric(1, 0))
    ActWhat = Column(String(70, 'Danish_Norwegian_CI_AS'))
    ActDone = Column(DateTime)
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'))
    OrderId = Column(String(20, 'Danish_Norwegian_CI_AS'))
    OrderPos = Column(Numeric(3, 0))
    Engineer = Column(String(30, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))
    LogM = Column(String(collation='Danish_Norwegian_CI_AS'))


class KabTrunk(Base):
    __tablename__ = 'KabTrunk'

    RowKey = Column(Integer, primary_key=True)
    TrunkCable = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    NumCores = Column(Numeric(5, 0))
    End_A = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    End_B = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    InUse = Column(DateTime)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))


class KabVia(Base):
    __tablename__ = 'KabVia'
    __table_args__ = (
        Index('TM_0106', 'Cable', 'Lvl', 'End', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    Cable = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Lvl = Column(Numeric(4, 0), nullable=False)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    HasCoil = Column(Numeric(1, 0))
    CoilLength = Column(Numeric(4, 0))
    CoilType = Column(String(10, 'Danish_Norwegian_CI_AS'))
    CoilStatus = Column(String(1, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class Order(Base):
    __tablename__ = 'Orders'

    RowKey = Column(Integer, primary_key=True)
    OrderId = Column(String(20, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    OrderTxt = Column(String(70, 'Danish_Norwegian_CI_AS'))
    Type = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Orderer = Column(String(15, 'Danish_Norwegian_CI_AS'))
    CaseHand = Column(String(15, 'Danish_Norwegian_CI_AS'))
    CustId = Column(String(18, 'Danish_Norwegian_CI_AS'))
    CuCaseHand = Column(String(15, 'Danish_Norwegian_CI_AS'))
    CuPhone = Column(String(15, 'Danish_Norwegian_CI_AS'))
    CuEMail = Column(String(35, 'Danish_Norwegian_CI_AS'))
    DtOrdered = Column(DateTime)
    DtOrdDeliv = Column(DateTime)
    DtDeliverd = Column(DateTime)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))


class PipeCab(Base):
    __tablename__ = 'PipeCab'
    __table_args__ = (
        Index('TM_0148', 'Cable', 'PipeMain', 'PipeSub', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    Cable = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    PipeMain = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, index=True)
    PipeSub = Column(String(25, 'Danish_Norwegian_CI_AS'), nullable=False)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class PipeMain(Base):
    __tablename__ = 'PipeMain'

    RowKey = Column(Integer, primary_key=True)
    PipeMain = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    Type = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'))
    End_A = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    End_B = Column(String(30, 'Danish_Norwegian_CI_AS'), index=True)
    Length = Column(Numeric(8, 0))
    InUse = Column(DateTime)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    ExtSysTxt = Column(String(30, 'Danish_Norwegian_CI_AS'))
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    PolylineM = Column(String(collation='Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))
    Status = Column(String(10, 'Danish_Norwegian_CI_AS'))


class PipeSpli(Base):
    __tablename__ = 'PipeSpli'
    __table_args__ = (
        Index('TM_0147', 'PipeMain2', 'PipeSub2'),
        Index('TM_0146', 'PipeMain1', 'PipeSub1'),
        Index('TM_0145', 'End', 'PipeMain1', 'PipeSub1')
    )

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    PipeMain1 = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    PipeSub1 = Column(String(25, 'Danish_Norwegian_CI_AS'), nullable=False)
    PipeMain2 = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    PipeSub2 = Column(String(25, 'Danish_Norwegian_CI_AS'), nullable=False)
    SpliceType = Column(Numeric(2, 0), nullable=False)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class PipeSub(Base):
    __tablename__ = 'PipeSub'
    __table_args__ = (
        Index('TM_0143', 'PipeMain', 'PipeSub', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    PipeMain = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    PipeSub = Column(String(25, 'Danish_Norwegian_CI_AS'), nullable=False)
    Type = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Diameter = Column(String(9, 'Danish_Norwegian_CI_AS'))
    Max_Cab = Column(Numeric(8, 0))
    EMCsens = Column(Numeric(1, 0))
    Owner = Column(String(10, 'Danish_Norwegian_CI_AS'))
    InUse = Column(DateTime)
    Reference = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    Cut_A = Column(Numeric(3, 0))
    Row_A = Column(Numeric(4, 0))
    Col_A = Column(Numeric(4, 0))
    Cut_B = Column(Numeric(3, 0))
    Row_B = Column(Numeric(4, 0))
    Col_B = Column(Numeric(4, 0))
    CustId = Column(String(18, 'Danish_Norwegian_CI_AS'), index=True)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class ProjWiz(Base):
    __tablename__ = 'ProjWiz'

    RowKey = Column(Integer, primary_key=True)
    Is_Project = Column(Numeric(1, 0))
    PNet_Type = Column(Numeric(1, 0))
    PAddress1 = Column(String(30, 'Danish_Norwegian_CI_AS'))
    PAddress2 = Column(String(30, 'Danish_Norwegian_CI_AS'))
    PBuildNumb = Column(String(4, 'Danish_Norwegian_CI_AS'))
    PFin_Date = Column(DateTime)
    PSh_Digits = Column(Numeric(1, 0))
    PCityLines = Column(Numeric(3, 0))
    PGrSnSkap = Column(Numeric(1, 0))
    PIs_Import = Column(Numeric(1, 0))
    PImp_Path = Column(String(254, 'Danish_Norwegian_CI_AS'))
    Is_Cnf = Column(Numeric(1, 0))
    Cnf_Id = Column(Numeric(2, 0))
    Cnf_Text = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Is_MDF = Column(Numeric(1, 0))
    MSerial = Column(String(8, 'Danish_Norwegian_CI_AS'))
    MType = Column(String(1, 'Danish_Norwegian_CI_AS'))
    MFloor = Column(Numeric(2, 0))
    MRoom = Column(String(5, 'Danish_Norwegian_CI_AS'))
    MDraw = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Is_Riser = Column(Numeric(1, 0))
    RRiser = Column(String(4, 'Danish_Norwegian_CI_AS'))
    RLen_HkTel = Column(Numeric(3, 0))
    RLen_HkCal = Column(Numeric(3, 0))
    RLen_HkDat = Column(Numeric(3, 0))
    RSkip_CC = Column(Numeric(1, 0))
    Is_CC = Column(Numeric(1, 0))
    CRiser = Column(String(4, 'Danish_Norwegian_CI_AS'))
    CFloor = Column(Numeric(2, 0))
    CSerial = Column(String(8, 'Danish_Norwegian_CI_AS'))
    CDraw = Column(String(5, 'Danish_Norwegian_CI_AS'))
    CRoom = Column(String(10, 'Danish_Norwegian_CI_AS'))
    Is_Floor = Column(Numeric(1, 0))
    FRiser = Column(String(4, 'Danish_Norwegian_CI_AS'))
    FFloor = Column(Numeric(2, 0))
    FFlo_CC = Column(Numeric(2, 0))
    FNumPoint = Column(Numeric(3, 0))
    FNumSparPt = Column(Numeric(3, 0))
    FLen_WP = Column(Numeric(3, 0))
    FTel = Column(Numeric(1, 0))
    FCal = Column(Numeric(1, 0))
    FDat = Column(Numeric(1, 0))
    FPat = Column(Numeric(1, 0))
    FFib = Column(Numeric(1, 0))
    FSkip_CC = Column(Numeric(1, 0))
    FSerial = Column(String(8, 'Danish_Norwegian_CI_AS'))
    FDraw = Column(String(10, 'Danish_Norwegian_CI_AS'))
    FRoom = Column(String(5, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class Project(Base):
    __tablename__ = 'Projects'

    RowKey = Column(Integer, primary_key=True)
    Project = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    Type = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Engineer = Column(String(30, 'Danish_Norwegian_CI_AS'))
    Vendor = Column(String(30, 'Danish_Norwegian_CI_AS'))
    CustId = Column(String(18, 'Danish_Norwegian_CI_AS'), index=True)
    Budget = Column(Numeric(10, 2))
    Ordered = Column(DateTime)
    StartDate = Column(DateTime)
    Completed = Column(DateTime)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    ExtSysTxt = Column(String(30, 'Danish_Norwegian_CI_AS'))
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Remark = Column(String(collation='Danish_Norwegian_CI_AS'))


class QuaranId(Base):
    __tablename__ = 'QuaranId'

    RowKey = Column(Integer, primary_key=True)
    RelToTbl = Column(String(1, 'Danish_Norwegian_CI_AS'), nullable=False)
    RelToKey = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    UpdVer = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class SbFei(Base):
    __tablename__ = 'SbFei'

    RowKey = Column(Integer, primary_key=True)
    FaultId = Column(Numeric(6, 0), nullable=False, unique=True)
    Circuit = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, index=True)
    DtReport = Column(DateTime)
    DtSolved = Column(DateTime)
    FaultDescr = Column(String(40, 'Danish_Norwegian_CI_AS'))
    FaultWas = Column(String(40, 'Danish_Norwegian_CI_AS'))
    Cable = Column(String(30, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))


class Service(Base):
    __tablename__ = 'Service'

    RowKey = Column(Integer, primary_key=True)
    Service = Column(String(12, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    Remark = Column(String(40, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class Setting(Base):
    __tablename__ = 'Settings'

    RowKey = Column(Integer, primary_key=True)
    VALUENAME = Column(String(70, 'Danish_Norwegian_CI_AS'), nullable=False)
    VALUEDATA = Column(String(254, 'Danish_Norwegian_CI_AS'))
    UPDVER = Column(Integer)
    INSWHEN = Column(DateTime)
    INSUSER = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UPDWHEN = Column(DateTime)
    UPDUSER = Column(String(20, 'Danish_Norwegian_CI_AS'))


class Standard(Base):
    __tablename__ = 'Standard'
    __table_args__ = (
        Index('TM_0161', 'Standard', 'Text', 'PartNo', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    Standard = Column(Numeric(3, 0), nullable=False)
    Text = Column(String(70, 'Danish_Norwegian_CI_AS'), nullable=False)
    PartNo = Column(String(20, 'Danish_Norwegian_CI_AS'), nullable=False)
    Text1 = Column(String(25, 'Danish_Norwegian_CI_AS'))
    Price = Column(Numeric(10, 2))
    MountTime = Column(Numeric(8, 2))
    Vendor = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Url = Column(String(254, 'Danish_Norwegian_CI_AS'))
    Remark = Column(String(45, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class UpdLog(Base):
    __tablename__ = 'UpdLog'

    RowKey = Column(Integer, primary_key=True)
    Type = Column(String(1, 'Danish_Norwegian_CI_AS'))
    Cmd = Column(String(1, 'Danish_Norwegian_CI_AS'))
    AppVer = Column(Integer)
    RecRowKey = Column(Integer)
    InsWhen = Column(DateTime, index=True)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RelToTbl = Column(String(1, 'Danish_Norwegian_CI_AS'))
    RelToKey = Column(String(30, 'Danish_Norwegian_CI_AS'))
    RelToTbl2 = Column(String(1, 'Danish_Norwegian_CI_AS'))
    RelToKey2 = Column(String(30, 'Danish_Norwegian_CI_AS'))
    RelToTbl3 = Column(String(1, 'Danish_Norwegian_CI_AS'))
    RelToKey3 = Column(String(30, 'Danish_Norwegian_CI_AS'))
    RelToTbl4 = Column(String(1, 'Danish_Norwegian_CI_AS'))
    RelToKey4 = Column(String(30, 'Danish_Norwegian_CI_AS'))
    RelToTbl5 = Column(String(1, 'Danish_Norwegian_CI_AS'))
    RelToKey5 = Column(String(30, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))


class UserTemp(Base):
    __tablename__ = 'UserTemp'

    RowKey = Column(Integer, primary_key=True)
    VALUENAME = Column(String(70, 'Danish_Norwegian_CI_AS'), nullable=False)
    VALUEDATA = Column(String(254, 'Danish_Norwegian_CI_AS'))
    UPDVER = Column(Integer)
    INSWHEN = Column(DateTime)
    INSUSER = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UPDWHEN = Column(DateTime)
    UPDUSER = Column(String(20, 'Danish_Norwegian_CI_AS'))


class UtsIP(Base):
    __tablename__ = 'UtsIP'
    __table_args__ = (
        Index('TM_0139', 'End', 'Card', 'Port', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Card = Column(String(22, 'Danish_Norwegian_CI_AS'))
    Port = Column(Numeric(4, 0))
    MACaddr = Column(String(17, 'Danish_Norwegian_CI_AS'))
    IPaddr = Column(String(39, 'Danish_Norwegian_CI_AS'))
    IP6addr = Column(String(39, 'Danish_Norwegian_CI_AS'))
    DNSname = Column(String(128, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))


class UtsKor(Base):
    __tablename__ = 'UtsKor'
    __table_args__ = (
        Index('TM_0134', 'End', 'Card', unique=True),
    )

    RowKey = Column(Integer, primary_key=True)
    End = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False)
    Card = Column(String(22, 'Danish_Norwegian_CI_AS'), nullable=False)
    Type = Column(String(20, 'Danish_Norwegian_CI_AS'))
    Virtual = Column(Numeric(1, 0))
    NumPorts = Column(Numeric(4, 0))
    Status = Column(String(10, 'Danish_Norwegian_CI_AS'))
    InUse = Column(DateTime)
    PortZerBas = Column(Numeric(1, 0))
    Position = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Setting = Column(String(15, 'Danish_Norwegian_CI_AS'))
    SerialNo = Column(String(25, 'Danish_Norwegian_CI_AS'))
    ServiceLvl = Column(String(1, 'Danish_Norwegian_CI_AS'))
    TrunkEq = Column(String(30, 'Danish_Norwegian_CI_AS'))
    TrunkEqOrd = Column(Integer)
    PS_Volt = Column(String(7, 'Danish_Norwegian_CI_AS'))
    PS_Psu1Cir = Column(String(12, 'Danish_Norwegian_CI_AS'))
    PS_Psu2Cir = Column(String(12, 'Danish_Norwegian_CI_AS'))
    PS_AveAmp = Column(Numeric(7, 1))
    PS_MaxAmp = Column(Numeric(7, 1))
    PS_NoHeat = Column(Numeric(1, 0))
    PS_BattAh = Column(Numeric(5, 0))
    PS_BattDt = Column(DateTime)
    InveNumb = Column(String(15, 'Danish_Norwegian_CI_AS'))
    InveOthLbl = Column(String(10, 'Danish_Norwegian_CI_AS'))
    InveIsLbld = Column(Numeric(1, 0))
    InveDtLtst = Column(DateTime)
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))


class Vendor(Base):
    __tablename__ = 'Vendor'

    RowKey = Column(Integer, primary_key=True)
    Vendor = Column(String(30, 'Danish_Norwegian_CI_AS'), nullable=False, unique=True)
    Phone = Column(String(15, 'Danish_Norwegian_CI_AS'))
    Email = Column(String(50, 'Danish_Norwegian_CI_AS'))
    OrgNum = Column(String(15, 'Danish_Norwegian_CI_AS'))
    UpdVer = Column(Integer)
    ExtSysId = Column(Integer)
    ExtSysId2 = Column(Integer)
    ExtSysId3 = Column(Integer)
    InsWhen = Column(DateTime)
    InsUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    UpdWhen = Column(DateTime)
    UpdUser = Column(String(20, 'Danish_Norwegian_CI_AS'))
    AddressM = Column(String(collation='Danish_Norwegian_CI_AS'))
    RemarkM = Column(String(collation='Danish_Norwegian_CI_AS'))


from cimgraph.data_profile.cimhub11.cimhub11 import (
    ACDCTerminal,
    ACLineSegment,
    ACLineSegmentPhase,
    ASTMStandard,
    AbnormalOPcatKind,
    AcceptanceTest,
    AccountNotification,
    Accumulator,
    AccumulatorLimit,
    AccumulatorLimitSet,
    AccumulatorReset,
    AccumulatorValue,
    ActivePowerLimit,
    ActivityRecord,
    AggregateScore,
    Agreement,
    AirCompressor,
    AlertTypeList,
    Analog,
    AnalogControl,
    AnalogLimit,
    AnalogLimitSet,
    AnalogValue,
    Analytic,
    AnalyticScore,
    ApparentPowerLimit,
    Appointment,
    Approver,
    Asset,
    AssetContainer,
    AssetDeployment,
    AssetFunction,
    AssetGroup,
    AssetHealthEvent,
    AssetInfo,
    AssetLocationHazard,
    AssetOrganisationRole,
    AssetOwner,
    AssetTestLab,
    AssetTestSampleTaker,
    AssetUser,
    AsynchronousMachine,
    AsynchronousMachineKind,
    AtmosphericAnalog,
    AtmosphericPhenomenon,
    Author,
    BaseFrequency,
    BasePower,
    BaseReading,
    BaseVoltage,
    BasicIntervalSchedule,
    BatteryUnit,
    Bay,
    BranchGroup,
    BranchGroupTerminal,
    Breaker,
    BreakerConfiguration,
    BusNameMarker,
    BusbarConfiguration,
    BusbarSection,
    BusbarSectionInfo,
    Bushing,
    BushingInfo,
    CAESPlant,
    CIGREStandard,
    Cabinet,
    CableInfo,
    CatalogAssetType,
    Channel,
    Clamp,
    TypeificationCondition,
    CloudCondition,
    CogenerationPlant,
    ComFunction,
    ComMedia,
    ComModule,
    CombinedCyclePlant,
    Command,
    CompositeSwitch,
    ConcentricNeutralCableInfo,
    ConductingEquipment,
    Conductor,
    ConfigurationEvent,
    ConformLoad,
    ConformLoadGroup,
    ConformLoadSchedule,
    ConnectivityNode,
    ConnectivityNodeContainer,
    Connector,
    ConstantPowerFactorSettingKind,
    ConstantPowerFactorSettings,
    ConstantReactivePowerSettings,
    Control,
    ControlledAppliance,
    CoordinateSystem,
    Crew,
    CrewMember,
    CrewType,
    Currency,
    CurrentLimit,
    Curve,
    CurveData,
    CurveStyle,
    Customer,
    CustomerAccount,
    CustomerAgreement,
    CustomerNotification,
    Cut,
    Cyclone,
    DERCurveData,
    DERDynamics,
    DERFunction,
    DERGroupDispatch,
    DERGroupForecast,
    DERIEEEType1,
    DERMonitorableParameter,
    DERNameplateData,
    DERNameplateDataApplied,
    DINStandard,
    DateInterval,
    DateTimeInterval,
    DayType,
    DecimalQuantity,
    DemandResponseProgram,
    DeploymentDate,
    DiagnosisDataSet,
    Disconnector,
    Discrete,
    DiscreteCommand,
    DiscreteValue,
    DispatchSchedule,
    DispatchablePowerCapability,
    DobleStandard,
    Document,
    DocumentPersonRole,
    DuctBank,
    DynamicsFunctionBlock,
    EPAStandard,
    EarthFaultCompensator,
    Earthquake,
    Editor,
    ElectronicAddress,
    EmissionAccount,
    EmissionCurve,
    EmissionType,
    EmissionValueSource,
    EndDevice,
    EndDeviceAction,
    EndDeviceCapability,
    EndDeviceControl,
    EndDeviceControlType,
    EndDeviceEvent,
    EndDeviceEventDetail,
    EndDeviceEventType,
    EndDeviceFunction,
    EndDeviceGroup,
    EndDeviceInfo,
    EndDeviceTiming,
    EnergyArea,
    EnergyConnection,
    EnergyConnectionProfile,
    EnergyConsumer,
    EnergyConsumerPhase,
    EnergySource,
    EnergySourcePhase,
    EnvironmentalAlert,
    EnvironmentalAnalog,
    EnvironmentalCodedValue,
    EnvironmentalDataAuthority,
    EnvironmentalDataProvider,
    EnvironmentalEvent,
    EnvironmentalInformation,
    EnvironmentalLocationType,
    EnvironmentalPhenomenon,
    EnvironmentalStringMeasurement,
    Equipment,
    EquipmentContainer,
    EquipmentFault,
    Estimate,
    ExtensionItem,
    ExtensionsList,
    ExternalNetworkInjection,
    FACTSDevice,
    Facility,
    FailureEvent,
    Fault,
    FaultCauseType,
    FaultImpedance,
    Feeder,
    FieldDispatchHistory,
    FieldDispatchStep,
    FinancialInfo,
    Fire,
    FloatQuantity,
    Flood,
    Forecast,
    FossilFuel,
    FrequencyConverter,
    FrequencyDroopSettings,
    FrequencyTripSettings,
    FuelAllocationSchedule,
    FuelType,
    Fuse,
    GenUnitOpCostCurve,
    GenUnitOpSchedule,
    GeneratingUnit,
    GeographicalRegion,
    GeosphericAnalog,
    GeosphericPhenomenon,
    GrossToNetActivePowerCurve,
    Ground,
    GroundDisconnector,
    GroundingImpedance,
    Hazard,
    HealthScore,
    HeatInputCurve,
    HeatRateCurve,
    House,
    Hurricane,
    HydroEnergyConversionKind,
    HydroGeneratingEfficiencyCurve,
    HydroGeneratingUnit,
    HydroPlantStorageKind,
    HydroPowerPlant,
    HydroPump,
    HydroPumpOpSchedule,
    HydrosphericAnalog,
    HydrosphericPhenomenon,
    IEC61968CIMVersion,
    IEC61970CIMVersion,
    IEC62325CIMVersion,
    IECStandard,
    IEEE1547ControlSettings,
    IEEE1547Info,
    IEEE1547Setting,
    IEEE1547TripSettings,
    IEEEStandard,
    IOPoint,
    ISOStandard,
    IdentifiedObject,
    InUseDate,
    IncidentHazard,
    IncrementalHeatRateCurve,
    InflowForecast,
    InspectionDataSet,
    IntegerQuantity,
    InterrupterUnit,
    InterrupterUnitInfo,
    IntervalBlock,
    IntervalReading,
    IrregularIntervalSchedule,
    IrregularTimePoint,
    Issuer,
    Joint,
    Jumper,
    Junction,
    LabTestDataSet,
    LaborelecStandard,
    Landslide,
    LevelVsVolumeCurve,
    LifecycleDate,
    LightningStrike,
    Limit,
    LimitSet,
    Line,
    LineFault,
    LinearShuntCompensator,
    LinearShuntCompensatorPhase,
    LoadArea,
    LoadBreakSwitch,
    LoadGroup,
    LoadResponseCharacteristic,
    Location,
    MagneticStorm,
    Maintainer,
    MaintenanceDataSet,
    Manufacturer,
    Measurement,
    MeasurementValue,
    MeasurementValueQuality,
    MeasurementValueSource,
    Medium,
    Meter,
    MeterMultiplier,
    MeterReading,
    MeterWorkTask,
    MetrologyRequirement,
    MomentaryCessationSettings,
    MonthDayInterval,
    MutualCoupling,
    Name,
    NameType,
    NameTypeAuthority,
    NamedPhenomenon,
    NoLoadTest,
    NonConformLoad,
    NonConformLoadGroup,
    NonConformLoadSchedule,
    NonlinearShuntCompensator,
    NonlinearShuntCompensatorPhase,
    NonlinearShuntCompensatorPhasePoint,
    NonlinearShuntCompensatorPoint,
    NormalOPcatKind,
    NuclearGeneratingUnit,
    Observation,
    OilSpecimen,
    OpenCircuitTest,
    OperatingMechanism,
    OperatingMechanismInfo,
    OperatingParticipant,
    OperatingShare,
    OperationPersonRole,
    OperationalLimit,
    OperationalLimitDirectionKind,
    OperationalLimitSet,
    OperationalLimitType,
    Operator,
    Organisation,
    OrganisationRole,
    OverfrequencyTripCurve,
    OverfrequencyTripCurveData,
    OverheadWireInfo,
    OvervoltageTripCurve,
    OvervoltageTripCurveData,
    Ownership,
    PSRType,
    PanDemandResponse,
    PanDisplay,
    PanPricing,
    PanPricingDetail,
    ParallelLineSegment,
    ParentOrganization,
    PendingCalculation,
    PenstockLossCurve,
    PerLengthImpedance,
    PerLengthLineParameter,
    PerLengthPhaseImpedance,
    PerLengthSequenceImpedance,
    Person,
    PersonRole,
    PetersenCoil,
    PetersenCoilModeKind,
    PhaseCode,
    PhaseConnectedFaultKind,
    PhaseImpedanceData,
    PhaseShuntConnectionKind,
    PhaseTapChanger,
    PhaseTapChangerAsymmetrical,
    PhaseTapChangerLinear,
    PhaseTapChangerNonLinear,
    PhaseTapChangerSymmetrical,
    PhaseTapChangerTable,
    PhaseTapChangerTablePoint,
    PhaseTapChangerTabular,
    PhenomenonTypeification,
    PhotovoltaicUnit,
    Plant,
    PositionPoint,
    PowerCutZone,
    PowerElectronicsConnection,
    PowerElectronicsConnectionPhase,
    PowerElectronicsUnit,
    PowerElectronicsWindUnit,
    PowerLimitSettings,
    PowerSystemResource,
    PowerTransformer,
    PowerTransformerEnd,
    PowerTransformerInfo,
    PricingStructure,
    Priority,
    Procedure,
    ProcedureDataSet,
    ProductAssetModel,
    ProtectedSwitch,
    Quality61850,
    RaiseLowerCommand,
    RatioTapChanger,
    RatioTapChangerTable,
    RatioTapChangerTablePoint,
    RationalNumber,
    ReactiveCapabilityCurve,
    Reading,
    ReadingInterharmonic,
    ReadingQuality,
    ReadingQualityType,
    ReadingType,
    Recloser,
    Register,
    RegularIntervalSchedule,
    RegularTimePoint,
    RegulatingCondEq,
    RegulatingControl,
    RegulatingControlModeKind,
    RegulationSchedule,
    RelativeDisplacement,
    RemoteInputSignal,
    ReportingCapability,
    ReportingGroup,
    ReportingSuperGroup,
    Reservoir,
    RightOfWay,
    RiskScore,
    RotatingMachine,
    SVCControlMode,
    ScheduledEvent,
    ScheduledEventData,
    Seal,
    Season,
    SeasonDayTypeSchedule,
    Sectionaliser,
    SeriesCompensator,
    ServiceCategory,
    ServiceLocation,
    ServiceMultiplier,
    ServiceSettings,
    SetPoint,
    ShortCircuitTest,
    ShuntCompensator,
    ShuntCompensatorInfo,
    ShuntCompensatorPhase,
    ShutdownCurve,
    SimpleEndDeviceFunction,
    SinglePhaseKind,
    SolarGeneratingUnit,
    SpaceAnalog,
    SpacePhenomenon,
    Specimen,
    StartIgnFuelCurve,
    StartMainFuelCurve,
    StartRampCurve,
    StartupModel,
    StateVariable,
    StaticVarCompensator,
    StationSupply,
    Status,
    SteamSendoutSchedule,
    StreetAddress,
    StreetDetail,
    Streetlight,
    StringMeasurement,
    StringMeasurementValue,
    StringQuantity,
    Structure,
    StructureSupport,
    SubGeographicalRegion,
    SubLoadArea,
    Substation,
    SvEstVoltage,
    SvInjection,
    SvPowerFlow,
    SvShuntCompensatorSections,
    SvStatus,
    SvSwitch,
    SvTapStep,
    SvVoltage,
    Switch,
    SwitchInfo,
    SwitchOperationSummary,
    SwitchPhase,
    SwitchSchedule,
    SynchronousMachine,
    SynchronousMachineKind,
    SynchronousMachineOperatingMode,
    TAPPIStandard,
    TailbayLossCurve,
    TapChanger,
    TapChangerControl,
    TapChangerInfo,
    TapChangerTablePoint,
    TapSchedule,
    TapeShieldCableInfo,
    TargetLevelSchedule,
    Tariff,
    TelephoneNumber,
    Terminal,
    TestDataSet,
    TestStandard,
    ThermalGeneratingUnit,
    ThermostatController,
    TimeInterval,
    TimePoint,
    TimeSchedule,
    TopologicalIsland,
    TopologicalNode,
    Tornado,
    TownDetail,
    TransformerCoreAdmittance,
    TransformerEnd,
    TransformerEndInfo,
    TransformerMeshImpedance,
    TransformerStarImpedance,
    TransformerTank,
    TransformerTankEnd,
    TransformerTankInfo,
    TransformerTest,
    TropicalCycloneAustralia,
    TroubleTicket,
    Tsunami,
    UKMinistryOfDefenceStandard,
    UnderfrequencyTripCurve,
    UnderfrequencyTripCurveData,
    UndervoltageTripCurve,
    UndervoltageTripCurveData,
    UnitMultiplier,
    UnitSymbol,
    UsagePoint,
    UsagePointGroup,
    UsagePointLocation,
    UserAttribute,
    Validity,
    ValueAliasSet,
    ValueToAlias,
    Version,
    VolcanicAshCloud,
    VoltVarCurve,
    VoltVarCurveData,
    VoltVarSettings,
    VoltWattCurve,
    VoltWattCurveData,
    VoltWattSettings,
    VoltageControlZone,
    VoltageLevel,
    VoltageLimit,
    VoltageTripSettings,
    WEPStandard,
    WattVarCurve,
    WattVarCurveData,
    WattVarSettings,
    Whirlpool,
    WindGenUnitKind,
    WindGeneratingUnit,
    WindingConnection,
    WireAssemblyInfo,
    WireInfo,
    WirePhaseInfo,
    WirePosition,
    WireSpacingInfo,
)

__all__ = [
    "ACDCTerminal",
    "ACLineSegment",
    "ACLineSegmentPhase",
    "ASTMStandard",
    "AbnormalOPcatKind",
    "AcceptanceTest",
    "AccountNotification",
    "Accumulator",
    "AccumulatorLimit",
    "AccumulatorLimitSet",
    "AccumulatorReset",
    "AccumulatorValue",
    "ActivePowerLimit",
    "ActivityRecord",
    "AggregateScore",
    "Agreement",
    "AirCompressor",
    "AlertTypeList",
    "Analog",
    "AnalogControl",
    "AnalogLimit",
    "AnalogLimitSet",
    "AnalogValue",
    "Analytic",
    "AnalyticScore",
    "ApparentPowerLimit",
    "Appointment",
    "Approver",
    "Asset",
    "AssetContainer",
    "AssetDeployment",
    "AssetFunction",
    "AssetGroup",
    "AssetHealthEvent",
    "AssetInfo",
    "AssetLocationHazard",
    "AssetOrganisationRole",
    "AssetOwner",
    "AssetTestLab",
    "AssetTestSampleTaker",
    "AssetUser",
    "AsynchronousMachine",
    "AsynchronousMachineKind",
    "AtmosphericAnalog",
    "AtmosphericPhenomenon",
    "Author",
    "BaseFrequency",
    "BasePower",
    "BaseReading",
    "BaseVoltage",
    "BasicIntervalSchedule",
    "BatteryUnit",
    "Bay",
    "BranchGroup",
    "BranchGroupTerminal",
    "Breaker",
    "BreakerConfiguration",
    "BusNameMarker",
    "BusbarConfiguration",
    "BusbarSection",
    "BusbarSectionInfo",
    "Bushing",
    "BushingInfo",
    "CAESPlant",
    "CIGREStandard",
    "Cabinet",
    "CableInfo",
    "CatalogAssetType",
    "Channel",
    "Clamp",
    "TypeificationCondition",
    "CloudCondition",
    "CogenerationPlant",
    "ComFunction",
    "ComMedia",
    "ComModule",
    "CombinedCyclePlant",
    "Command",
    "CompositeSwitch",
    "ConcentricNeutralCableInfo",
    "ConductingEquipment",
    "Conductor",
    "ConfigurationEvent",
    "ConformLoad",
    "ConformLoadGroup",
    "ConformLoadSchedule",
    "ConnectivityNode",
    "ConnectivityNodeContainer",
    "Connector",
    "ConstantPowerFactorSettingKind",
    "ConstantPowerFactorSettings",
    "ConstantReactivePowerSettings",
    "Control",
    "ControlledAppliance",
    "CoordinateSystem",
    "Crew",
    "CrewMember",
    "CrewType",
    "Currency",
    "CurrentLimit",
    "Curve",
    "CurveData",
    "CurveStyle",
    "Customer",
    "CustomerAccount",
    "CustomerAgreement",
    "CustomerNotification",
    "Cut",
    "Cyclone",
    "DERCurveData",
    "DERDynamics",
    "DERFunction",
    "DERGroupDispatch",
    "DERGroupForecast",
    "DERIEEEType1",
    "DERMonitorableParameter",
    "DERNameplateData",
    "DERNameplateDataApplied",
    "DINStandard",
    "DateInterval",
    "DateTimeInterval",
    "DayType",
    "DecimalQuantity",
    "DemandResponseProgram",
    "DeploymentDate",
    "DiagnosisDataSet",
    "Disconnector",
    "Discrete",
    "DiscreteCommand",
    "DiscreteValue",
    "DispatchSchedule",
    "DispatchablePowerCapability",
    "DobleStandard",
    "Document",
    "DocumentPersonRole",
    "DuctBank",
    "DynamicsFunctionBlock",
    "EPAStandard",
    "EarthFaultCompensator",
    "Earthquake",
    "Editor",
    "ElectronicAddress",
    "EmissionAccount",
    "EmissionCurve",
    "EmissionType",
    "EmissionValueSource",
    "EndDevice",
    "EndDeviceAction",
    "EndDeviceCapability",
    "EndDeviceControl",
    "EndDeviceControlType",
    "EndDeviceEvent",
    "EndDeviceEventDetail",
    "EndDeviceEventType",
    "EndDeviceFunction",
    "EndDeviceGroup",
    "EndDeviceInfo",
    "EndDeviceTiming",
    "EnergyArea",
    "EnergyConnection",
    "EnergyConnectionProfile",
    "EnergyConsumer",
    "EnergyConsumerPhase",
    "EnergySource",
    "EnergySourcePhase",
    "EnvironmentalAlert",
    "EnvironmentalAnalog",
    "EnvironmentalCodedValue",
    "EnvironmentalDataAuthority",
    "EnvironmentalDataProvider",
    "EnvironmentalEvent",
    "EnvironmentalInformation",
    "EnvironmentalLocationType",
    "EnvironmentalPhenomenon",
    "EnvironmentalStringMeasurement",
    "Equipment",
    "EquipmentContainer",
    "EquipmentFault",
    "Estimate",
    "ExtensionItem",
    "ExtensionsList",
    "ExternalNetworkInjection",
    "FACTSDevice",
    "Facility",
    "FailureEvent",
    "Fault",
    "FaultCauseType",
    "FaultImpedance",
    "Feeder",
    "FieldDispatchHistory",
    "FieldDispatchStep",
    "FinancialInfo",
    "Fire",
    "FloatQuantity",
    "Flood",
    "Forecast",
    "FossilFuel",
    "FrequencyConverter",
    "FrequencyDroopSettings",
    "FrequencyTripSettings",
    "FuelAllocationSchedule",
    "FuelType",
    "Fuse",
    "GenUnitOpCostCurve",
    "GenUnitOpSchedule",
    "GeneratingUnit",
    "GeographicalRegion",
    "GeosphericAnalog",
    "GeosphericPhenomenon",
    "GrossToNetActivePowerCurve",
    "Ground",
    "GroundDisconnector",
    "GroundingImpedance",
    "Hazard",
    "HealthScore",
    "HeatInputCurve",
    "HeatRateCurve",
    "House",
    "Hurricane",
    "HydroEnergyConversionKind",
    "HydroGeneratingEfficiencyCurve",
    "HydroGeneratingUnit",
    "HydroPlantStorageKind",
    "HydroPowerPlant",
    "HydroPump",
    "HydroPumpOpSchedule",
    "HydrosphericAnalog",
    "HydrosphericPhenomenon",
    "IEC61968CIMVersion",
    "IEC61970CIMVersion",
    "IEC62325CIMVersion",
    "IECStandard",
    "IEEE1547ControlSettings",
    "IEEE1547Info",
    "IEEE1547Setting",
    "IEEE1547TripSettings",
    "IEEEStandard",
    "IOPoint",
    "ISOStandard",
    "IdentifiedObject",
    "InUseDate",
    "IncidentHazard",
    "IncrementalHeatRateCurve",
    "InflowForecast",
    "InspectionDataSet",
    "IntegerQuantity",
    "InterrupterUnit",
    "InterrupterUnitInfo",
    "IntervalBlock",
    "IntervalReading",
    "IrregularIntervalSchedule",
    "IrregularTimePoint",
    "Issuer",
    "Joint",
    "Jumper",
    "Junction",
    "LabTestDataSet",
    "LaborelecStandard",
    "Landslide",
    "LevelVsVolumeCurve",
    "LifecycleDate",
    "LightningStrike",
    "Limit",
    "LimitSet",
    "Line",
    "LineFault",
    "LinearShuntCompensator",
    "LinearShuntCompensatorPhase",
    "LoadArea",
    "LoadBreakSwitch",
    "LoadGroup",
    "LoadResponseCharacteristic",
    "Location",
    "MagneticStorm",
    "Maintainer",
    "MaintenanceDataSet",
    "Manufacturer",
    "Measurement",
    "MeasurementValue",
    "MeasurementValueQuality",
    "MeasurementValueSource",
    "Medium",
    "Meter",
    "MeterMultiplier",
    "MeterReading",
    "MeterWorkTask",
    "MetrologyRequirement",
    "MomentaryCessationSettings",
    "MonthDayInterval",
    "MutualCoupling",
    "Name",
    "NameType",
    "NameTypeAuthority",
    "NamedPhenomenon",
    "NoLoadTest",
    "NonConformLoad",
    "NonConformLoadGroup",
    "NonConformLoadSchedule",
    "NonlinearShuntCompensator",
    "NonlinearShuntCompensatorPhase",
    "NonlinearShuntCompensatorPhasePoint",
    "NonlinearShuntCompensatorPoint",
    "NormalOPcatKind",
    "NuclearGeneratingUnit",
    "Observation",
    "OilSpecimen",
    "OpenCircuitTest",
    "OperatingMechanism",
    "OperatingMechanismInfo",
    "OperatingParticipant",
    "OperatingShare",
    "OperationPersonRole",
    "OperationalLimit",
    "OperationalLimitDirectionKind",
    "OperationalLimitSet",
    "OperationalLimitType",
    "Operator",
    "Organisation",
    "OrganisationRole",
    "OverfrequencyTripCurve",
    "OverfrequencyTripCurveData",
    "OverheadWireInfo",
    "OvervoltageTripCurve",
    "OvervoltageTripCurveData",
    "Ownership",
    "PSRType",
    "PanDemandResponse",
    "PanDisplay",
    "PanPricing",
    "PanPricingDetail",
    "ParallelLineSegment",
    "ParentOrganization",
    "PendingCalculation",
    "PenstockLossCurve",
    "PerLengthImpedance",
    "PerLengthLineParameter",
    "PerLengthPhaseImpedance",
    "PerLengthSequenceImpedance",
    "Person",
    "PersonRole",
    "PetersenCoil",
    "PetersenCoilModeKind",
    "PhaseCode",
    "PhaseConnectedFaultKind",
    "PhaseImpedanceData",
    "PhaseShuntConnectionKind",
    "PhaseTapChanger",
    "PhaseTapChangerAsymmetrical",
    "PhaseTapChangerLinear",
    "PhaseTapChangerNonLinear",
    "PhaseTapChangerSymmetrical",
    "PhaseTapChangerTable",
    "PhaseTapChangerTablePoint",
    "PhaseTapChangerTabular",
    "PhenomenonTypeification",
    "PhotovoltaicUnit",
    "Plant",
    "PositionPoint",
    "PowerCutZone",
    "PowerElectronicsConnection",
    "PowerElectronicsConnectionPhase",
    "PowerElectronicsUnit",
    "PowerElectronicsWindUnit",
    "PowerLimitSettings",
    "PowerSystemResource",
    "PowerTransformer",
    "PowerTransformerEnd",
    "PowerTransformerInfo",
    "PricingStructure",
    "Priority",
    "Procedure",
    "ProcedureDataSet",
    "ProductAssetModel",
    "ProtectedSwitch",
    "Quality61850",
    "RaiseLowerCommand",
    "RatioTapChanger",
    "RatioTapChangerTable",
    "RatioTapChangerTablePoint",
    "RationalNumber",
    "ReactiveCapabilityCurve",
    "Reading",
    "ReadingInterharmonic",
    "ReadingQuality",
    "ReadingQualityType",
    "ReadingType",
    "Recloser",
    "Register",
    "RegularIntervalSchedule",
    "RegularTimePoint",
    "RegulatingCondEq",
    "RegulatingControl",
    "RegulatingControlModeKind",
    "RegulationSchedule",
    "RelativeDisplacement",
    "RemoteInputSignal",
    "ReportingCapability",
    "ReportingGroup",
    "ReportingSuperGroup",
    "Reservoir",
    "RightOfWay",
    "RiskScore",
    "RotatingMachine",
    "SVCControlMode",
    "ScheduledEvent",
    "ScheduledEventData",
    "Seal",
    "Season",
    "SeasonDayTypeSchedule",
    "Sectionaliser",
    "SeriesCompensator",
    "ServiceCategory",
    "ServiceLocation",
    "ServiceMultiplier",
    "ServiceSettings",
    "SetPoint",
    "ShortCircuitTest",
    "ShuntCompensator",
    "ShuntCompensatorInfo",
    "ShuntCompensatorPhase",
    "ShutdownCurve",
    "SimpleEndDeviceFunction",
    "SinglePhaseKind",
    "SolarGeneratingUnit",
    "SpaceAnalog",
    "SpacePhenomenon",
    "Specimen",
    "StartIgnFuelCurve",
    "StartMainFuelCurve",
    "StartRampCurve",
    "StartupModel",
    "StateVariable",
    "StaticVarCompensator",
    "StationSupply",
    "Status",
    "SteamSendoutSchedule",
    "StreetAddress",
    "StreetDetail",
    "Streetlight",
    "StringMeasurement",
    "StringMeasurementValue",
    "StringQuantity",
    "Structure",
    "StructureSupport",
    "SubGeographicalRegion",
    "SubLoadArea",
    "Substation",
    "SvEstVoltage",
    "SvInjection",
    "SvPowerFlow",
    "SvShuntCompensatorSections",
    "SvStatus",
    "SvSwitch",
    "SvTapStep",
    "SvVoltage",
    "Switch",
    "SwitchInfo",
    "SwitchOperationSummary",
    "SwitchPhase",
    "SwitchSchedule",
    "SynchronousMachine",
    "SynchronousMachineKind",
    "SynchronousMachineOperatingMode",
    "TAPPIStandard",
    "TailbayLossCurve",
    "TapChanger",
    "TapChangerControl",
    "TapChangerInfo",
    "TapChangerTablePoint",
    "TapSchedule",
    "TapeShieldCableInfo",
    "TargetLevelSchedule",
    "Tariff",
    "TelephoneNumber",
    "Terminal",
    "TestDataSet",
    "TestStandard",
    "ThermalGeneratingUnit",
    "ThermostatController",
    "TimeInterval",
    "TimePoint",
    "TimeSchedule",
    "TopologicalIsland",
    "TopologicalNode",
    "Tornado",
    "TownDetail",
    "TransformerCoreAdmittance",
    "TransformerEnd",
    "TransformerEndInfo",
    "TransformerMeshImpedance",
    "TransformerStarImpedance",
    "TransformerTank",
    "TransformerTankEnd",
    "TransformerTankInfo",
    "TransformerTest",
    "TropicalCycloneAustralia",
    "TroubleTicket",
    "Tsunami",
    "UKMinistryOfDefenceStandard",
    "UnderfrequencyTripCurve",
    "UnderfrequencyTripCurveData",
    "UndervoltageTripCurve",
    "UndervoltageTripCurveData",
    "UnitMultiplier",
    "UnitSymbol",
    "UsagePoint",
    "UsagePointGroup",
    "UsagePointLocation",
    "UserAttribute",
    "Validity",
    "ValueAliasSet",
    "ValueToAlias",
    "Version",
    "VolcanicAshCloud",
    "VoltVarCurve",
    "VoltVarCurveData",
    "VoltVarSettings",
    "VoltWattCurve",
    "VoltWattCurveData",
    "VoltWattSettings",
    "VoltageControlZone",
    "VoltageLevel",
    "VoltageLimit",
    "VoltageTripSettings",
    "WEPStandard",
    "WattVarCurve",
    "WattVarCurveData",
    "WattVarSettings",
    "Whirlpool",
    "WindGenUnitKind",
    "WindGeneratingUnit",
    "WindingConnection",
    "WireAssemblyInfo",
    "WireInfo",
    "WirePhaseInfo",
    "WirePosition",
    "WireSpacingInfo",
]

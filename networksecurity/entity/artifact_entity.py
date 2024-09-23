from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    pass

@dataclass
class DataValidationArtifact:
    trained_file_path: str
    test_file_path: str

@dataclass
class DataTransformationArtifact:
    pass

@dataclass
class ModelTrainerArtifact:
    pass

@dataclass
class ModelEvaluationArtifact:
    pass

@dataclass
class ModelPusherArtifact:
    pass 
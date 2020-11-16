# Paul Le
# Oct 25, 2020
# CS A131
# Zip Code Parser


class ZipCode:
    def __init__(self, newZip: str, newFIPS: int, newDistrict: int,
                 newState: str):
        self.zipCode = newZip
        self.FIPS = newFIPS
        self.district = newDistrict
        self.state = newState

    def setZip(self, newZip: str) -> None:
        "changes self's zip code info"
        self.zipCode = newZip

    def setFIPS(self, newFIPS: int) -> None:
        "changes self's FIPS code"
        self.FIPS = newFIPS
        
    def setDistrict(self, newDistrict: int) -> None:
        "changes self's district number"
        self.district = newDistrict

    def setState(self, newState: str) -> None:
        "changes self's state"
        self.state = newState

    def getZip(self) -> str:
        "returns self's zip code info"
        return self.zipCode

    def getFIPS(self) -> int:
        "returns self's FIPS code"
        return self.FIPS

    def getDistrict(self) -> int:
        "returns self's district number"
        return self.district

    def getState(self) -> str:
        "returns self's state"
        return self.state

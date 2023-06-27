from src.core.constants import SERVICE_FEE_PERCENT


def get_service_charge(amount):
    return (SERVICE_FEE_PERCENT * amount) // 100

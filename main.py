from src.augmented_reality_service import AugmentedRealityService


if __name__ == "__main__":

    # Starting AR Service
    ar_service = AugmentedRealityService()
    ar_service.set_service_parameter_json("data/aruco_params.json")
    ar_service.run_service()


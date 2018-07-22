from augmented_reality_service import AugmentedRealityService


if __name__ == "__main__":

    ar_service = AugmentedRealityService()

    ar_service.set_service_parameter_json("data/params.json")
    ar_service.run_service()


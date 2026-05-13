def evaluate_selectivity(
    upstream_breaker_a: float,
    downstream_breaker_a: float
):

    ratio = (
        upstream_breaker_a
        / downstream_breaker_a
    )

    if ratio >= 1.6:

        return {
            "selective": True,
            "status": "Good selectivity"
        }

    if ratio >= 1.3:

        return {
            "selective": "partial",
            "status": "Partial selectivity"
        }

    return {
        "selective": False,
        "status": "Poor selectivity"
    }


def evaluate_backup_protection(
    upstream_icu_ka: float,
    downstream_fault_ka: float
):

    if upstream_icu_ka >= downstream_fault_ka:

        return {
            "backup_protection": True,
            "status": "Backup protection valid"
        }

    return {
        "backup_protection": False,
        "status": "Insufficient upstream breaking capacity"
    }

from ga4gh.htsget.compliance.config import constants as c

TEST_GROUPS = {
    "reads": {
        "cases": [
            {
                "name": "get htsget ticket 1",
                "url": c.READS_URL,
                "obj_id": c.READS_ID_FOUND_1
            },
            {
                "name": "get htsget ticket 2",
                "url": c.READS_URL,
                "obj_id": c.READS_ID_FOUND_2
            }
        ]
    },
    "variants": {
        "cases": [

        ]
    }
}
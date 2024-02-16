import pull_request_comment
import logging
import json
import pandas as pd

logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] - %(message)s", force=True
)


def main():
    """Create a Pull Request comment within azure-pipelines-pr.yml"."""
    msg = pull_request_comment.Message()

    try:
        with open("./cdk.out/policy-validation-report.json", "r") as report:
            report_dict = json.load(report)
        df = pd.DataFrame.from_dict(report_dict["pluginReports"][0]["violations"])
        df = df.drop(["violatingConstructs", "ruleMetadata"], axis=1)
    except IndexError as e:
        logging.exception(e)
        logging.exception(report_dict)
        df = pd.DataFrame.from_dict([{"ValdidationErrors": "None"}])
        
    logging.info("Adding CDK Validation report")
    msg.add(comment=df.to_markdown())

if __name__ == "__main__":
    main()

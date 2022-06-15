from telco_churn.common import Job
from telco_churn.model_inference import ModelInference
from telco_churn.utils.logger_utils import get_logger

_logger = get_logger()


class ModelInferenceJob(Job):

    def launch(self):
        _logger.info('Launching Batch ModelInferenceJob job')
        model_registry_name = self.conf['mlflow_params']['model_registry_name']
        model_registry_stage = self.conf['mlflow_params']['model_registry_stage']
        model_uri = f'models:/{model_registry_name}/{model_registry_stage}'

        ModelInference(model_uri=model_uri,
                       inference_data=self.conf['data_input']['table_name'])\
            .run_and_write_batch(delta_path=self.conf['data_output']['delta_path'],
                                 table_name=self.conf['data_output']['table_name'],
                                 mode=self.conf['data_output']['mode'])
        _logger.info('Batch ModelInferenceJob job finished')


if __name__ == "__main__":
    job = ModelInferenceJob()
    job.launch()

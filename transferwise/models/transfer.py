from transferwise.models.base import TFModel


class TransferRequirements(TFModel):
    """
    SEE https://api-docs.transferwise.com/#transfers-requirements
    """
    target_account = None  # Account model
    quote = None  # Quote model
    details = None  # dict with transfer details for transfer verification
    customer_transaction_id = None  # generated UUID for request idempotency


class Transfer(TFModel):
    _entity = 'transfers'
    target_account = None  # Account model
    quote = None  # Quote model
    customer_transaction_id = None  # generated UUID for request idempotency
    details = None  # dict with transfer details

    def verify(self, requirements: TransferRequirements):
        """
        Verify transfer data
        Raises an exception if verification didn't pass
        """
        pass

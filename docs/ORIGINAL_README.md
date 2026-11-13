# IT Helpdesk Ticket Classifier

Classifies incoming helpdesk tickets into service categories and estimates an operational priority using transparent urgency/impact rules.

## Train
```bash
pip install -r requirements.txt
python src/train.py sample/tickets.csv --model outputs/ticket_model.joblib
```

## Predict
```bash
python src/predict.py outputs/ticket_model.joblib   "VPN unavailable for the entire finance team; month-end work is blocked"
```

The priority rule is intentionally explainable and should be adapted to an organization's service-management policy.

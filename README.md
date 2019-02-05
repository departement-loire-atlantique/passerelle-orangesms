# passerelle-orangesms

Connecteur Publik Passerelle pour le service d'envoi de SMS Orange Contact Everyone REST API v1.2.

## Installation

pip install git+https://github.com/departement-loire-atlantique/passerelle-orangesms#egg=passerelle-orangesms

Ajouter l'application dans les paramètres de passerelle. 
Par exemple, dans `/etc/passerelle/settings.d/loire-atlantique.py`, ajouter :

```
    INSTALLED_APPS += ('passerelle-orangesms',)
    TENANT_APPS += ('passerelle-orangesms',)
```


## Mise à jour

pip install passerelle-orangesms --upgrade

## Désinstallation

pip uninstall passerelle-orangesms

# OBSOLÈTE - ce connecteur n'a plus d'utilité, Entr'ouvert l'ayant intégré dans Publik.

# passerelle-orangesms

Connecteur Publik Passerelle pour le service d'envoi de SMS Orange Contact Everyone REST API v1.2.

## Installation

```
pip install git+https://github.com/departement-loire-atlantique/passerelle-orangesms#egg=passerelle-orangesms
```

Le script doit être exécuté en root car il déploie automatiquement l'application dans passerelle en créant le fichier
`/etc/passerelle/settings.d/passerelle-orangesms.py`.

## Configuration dans Publik

Dans le menu *Services web*, ajouter un connecteur. Choisir comme fournisseur SMS *Orange REST SMS*, et saisir les paramètres du service (titre, description, etc).

Ensuite, dans le menu *Paramètres / SMS*, indiquer dans les options SMS :

- Mode SMS : Fournisseur Passerelle
- Expéditeur : Un nom ou un numéro (n'a pas d'importance car n'apparaîtra pas dans les envois de SMS)
- URL : `[passerelle_url]/passerelle-orangesms/sms-orange/send`

Il est possible de tester le fonctionnement des envois avec le lien *Test SMS* disponible sur cette page des options SMS.

## Utilisation dans un worklow

Une fois la configuration dans Publik effectuée, l'action de workflow "SMS" est disponible pour les workflows.

L'action de workflow "SMS" est liée au service web Orange REST SMS configuré dans l'instance Publik. Il n'est pas possible de créer plusieurs types d'actions de workflow "SMS" liés pour chacun à un compte dédié de l'API SMS Orange. S'il est nécessaire d'avoir des envois de SMS avec plusieurs comptes, la solution est d'utiliser directement le service web Orange en passant par une action de worklow "Webservice" plutôt que "SMS".

## Désinstallation

```
pip uninstall passerelle-orangesms
rm /etc/passerelle/settings.d/passerelle-orangesms.py
```

## Release

Pour marquer le commit b4dda3fbd58e en tant que version 0.5, faire:

```
git tag -a v0.5 b4dda3fbd58e
git push origin v0.5
```

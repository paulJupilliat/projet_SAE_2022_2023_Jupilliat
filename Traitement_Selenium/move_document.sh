#!/bin/bash
if (( $# == 1));
then
    mv ~/Téléchargements/"${1}" ./Traitement_Selenium;
fi
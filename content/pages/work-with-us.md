title: Lavora con Noi
date: 2022-01-31 10:22
save_as: work-with-us.html
url: work-with-us.html
menu_order: 1

{% from 'row.html' import row %}
{% from 'row.html' import hero %}

{{ hero("Lavora con Noi",
    "MGALabs offre attività di alta qualità, allo stato dell'arte della cybersecurity, senza nessun compromesso.
    Per fare questo ricerchiamo professionisti della sicurezza informatica, ma non solo, ricerchiamo hacker appassionati e studiosi. Crediamo fermamente nello sviluppo della conoscienza, l'ambiente è sviluppato per favorire lo scambio di esperienze e lo sviluppo professionale, anche con specifici piani di training e certificazione.",
    "/images/work-with-us.png",
    "Lavora con Noi") }}

## Posizioni Aperte

{{ row("Red Team Member",
    "Ricerchiamo uno specialista in offensive security da inserire all'interno del nostro Red Team, possibilmente
    con esperienza in penetration testing su web application , mobile application o infrastruttura. 
    RAL commisurata alla seniority. 
    </p>
    <a class='btn btn-outline btn-orange my-3' href='mailto:info@mgalabs.com?subject=Red Team' target='_blank'>Invia Candidatura</a>
    ",
    "",
    "")
}}

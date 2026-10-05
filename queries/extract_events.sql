SELECT document_ref,
       status,
       changed_at
FROM document_status_history
ORDER BY document_ref, changed_at;

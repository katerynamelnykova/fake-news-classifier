from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


def classification_summary(y_test, y_pred, cmap="Purples", digits=5, title="Confusion Matrix"):
    """
    Prints a classification report and displays a confusion matrix for binary classification.

    Parameters
    ----------
    y_test : array-like
        True class labels.
    y_pred : array-like
        Predicted class labels.
    cmap : str, optional
        Colormap for the confusion matrix plot. Default is 'Purples'.
    digits : int, optional
        Number of decimal places for classification metrics. Default is 5.
    title : str, optional
        Title for the confusion matrix plot. Default is 'Confusion Matrix'.

    Returns
    -------
    None
    """

    print("Classification Report:")
    print(classification_report(y_test, y_pred, digits=digits))

    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1])
    disp.plot(cmap=cmap)
    plt.title(title)
    plt.tight_layout()
    plt.show()
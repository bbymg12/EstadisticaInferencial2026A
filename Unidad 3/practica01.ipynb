{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNSMK1ihdgf+80vHaV2WfqU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DrFaus/Estadistica2026B/blob/main/Practica01U3.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Práctica 01 para series de tiempo"
      ],
      "metadata": {
        "id": "GISE7g3siFiV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Para esta práctica, se utilizará la librería `yfinance`, la cual permite obtener datos históricos de mercados financieros directamente desde Yahoo Finance. Esta herramienta es de uso gratuito y no requiere el uso de claves de acceso (API keys), lo que la hace especialmente conveniente para fines educativos.\n",
        "\n",
        "Los datos obtenidos mediante `yfinance` corresponden a información real del mercado financiero. Sin embargo, es importante considerar que esta herramienta no constituye una fuente oficial de datos, por lo que puede presentar limitaciones en cuanto a disponibilidad, consistencia o actualización. Para fines académicos y de análisis exploratorio, estos datos son adecuados; no obstante, para aplicaciones profesionales o decisiones financieras, se recomienda el uso de fuentes oficiales o servicios especializados.\n",
        "\n",
        "Adicionalmente, `yfinance` no es una API oficial, por lo que en ocasiones puede presentar fallas temporales en la descarga de datos.\n",
        "\n",
        "Los principales argumentos que requiere yfinance para realizar la descarga son:\n",
        "\n",
        "+ `tickers`: Los tickers son identificadores únicos de activos financieros (por ejemplo, acciones) en los mercados. Por ejemplo, `AAPL` corresponde a Apple, `TSLA` a Tesla y `MSFT` a Microsoft. Si quieres inspeccionar tickers [pulsa aquí](https://www.nasdaq.com/market-activity/stocks/screener) y se te abrirá un catálogo de diversas multinacionales.\n",
        "+ `start`: Fecha de inicio para la descarga de datos en formato `YYYY-mm-dd` que significa: cuatro dígitos para el año (`YYYY`), dos dígitos para el mes (`mm`) y dos dígitos para el día (`dd`) en ese orden.\n",
        "+ `end`: Fecha de fin para la descarga de datos siguiendo también un formato `YYYY-mm-dd`.\n",
        "+ `interval`: Define la frecuencia de los datos. Por ejemplo, `\"1d\"` indica datos diarios, `\"1wk\"` semanales y `\"1mo\"` mensuales.\n",
        "+ `group_by`: Define la forma en que se organizan las columnas cuando se descargan datos de uno o varios tickers. Por ejemplo, `group_by=\"column\"` organiza la información por tipo de variable (Open, High, Low, Close, etc.), mientras que `group_by=\"ticker\"` agrupa primero por activo financiero.\n",
        "+ `auto_adjust`: Si se establece en `True`, los precios se ajustan automáticamente considerando dividendos y divisiones de acciones. Si es `False`, se mantienen los valores originales.\n",
        "+ `actions`: Permite incluir información adicional como dividendos y divisiones de acciones cuando se establece en `True`.\n",
        "+ `progress`: Controla si se muestra o no una barra de progreso durante la descarga."
      ],
      "metadata": {
        "id": "63LhegtMk9wv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import yfinance as yf\n",
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")\n",
        "\n",
        "# Link para inspeccionar tickers:\n",
        "# https://www.nasdaq.com/market-activity/stocks/screener\n",
        "\n",
        "# Obtener datos de acciones\n",
        "df = yf.download(\n",
        "    tickers=\"AAPL\",          # AAPL: Apple, TSLA: Tesla, MSFT: Microsoft, etc.\n",
        "    start=\"2024-01-01\",      # Fecha de inicio\n",
        "    end=\"2026-04-01\",        # Fecha de fin\n",
        "    interval=\"1d\",           # Intervalo de tiempo: 1 día\n",
        "    group_by=\"column\",       # Forma estándar de organizar las columnas\n",
        "    auto_adjust=False,       # False conserva columnas como Close y Adj Close\n",
        "    actions=False,           # True incluiría dividendos y divisiones de acciones\n",
        "    progress=False           # Evita mostrar barra de progreso\n",
        ")\n",
        "\n",
        "# Verificar si la descarga fue exitosa\n",
        "if df.empty:\n",
        "    raise ValueError(\n",
        "        \"No se descargaron datos. Verifica que el ticker sea correcto \"\n",
        "        \"o intenta nuevamente más tarde.\"\n",
        "    )\n",
        "\n",
        "# Paso 1: Mover 'Date' del índice a columna regular\n",
        "df = df.reset_index()\n",
        "\n",
        "# Paso 2: Aplanar columnas si vienen como MultiIndex\n",
        "# Esto puede ocurrir dependiendo de la versión de yfinance/pandas.\n",
        "if isinstance(df.columns, pd.MultiIndex):\n",
        "    df.columns = [\n",
        "        \"_\".join([str(valor) for valor in columna if valor != \"\"]).strip()\n",
        "        for columna in df.columns\n",
        "    ]\n",
        "\n",
        "# Reemplazar espacios por _\n",
        "df.columns = [i.replace(\" \", \"_\") for i in df.columns]\n",
        "\n",
        "# Paso 3:\n",
        "#######################################################\n",
        "## En caso de que no se requiera la hora\n",
        "\n",
        "# Convertir la columna 'Date' a tipo datetime\n",
        "df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')\n",
        "\n",
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "0qgLXpmCjjkx",
        "outputId": "a2612527-edc5-4cf8-b4a0-539daebef192"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          Date  Adj_Close_AAPL  Close_AAPL   High_AAPL    Low_AAPL  \\\n",
              "0   2024-01-02      183.731308  185.639999  188.440002  183.889999   \n",
              "1   2024-01-03      182.355591  184.250000  185.880005  183.429993   \n",
              "2   2024-01-04      180.039658  181.910004  183.089996  180.880005   \n",
              "3   2024-01-05      179.317184  181.179993  182.759995  180.169998   \n",
              "4   2024-01-08      183.652130  185.559998  185.600006  181.500000   \n",
              "..         ...             ...         ...         ...         ...   \n",
              "558 2026-03-25      252.619995  252.619995  255.000000  251.600006   \n",
              "559 2026-03-26      252.889999  252.889999  257.000000  250.770004   \n",
              "560 2026-03-27      248.800003  248.800003  255.490005  248.070007   \n",
              "561 2026-03-30      246.630005  246.630005  250.869995  245.509995   \n",
              "562 2026-03-31      253.789993  253.789993  255.479996  247.100006   \n",
              "\n",
              "      Open_AAPL  Volume_AAPL  \n",
              "0    187.149994     82488700  \n",
              "1    184.220001     58414500  \n",
              "2    182.149994     71983600  \n",
              "3    181.990005     62379700  \n",
              "4    182.089996     59144500  \n",
              "..          ...          ...  \n",
              "558  254.100006     28476700  \n",
              "559  252.119995     41796700  \n",
              "560  253.899994     47900000  \n",
              "561  250.070007     39446200  \n",
              "562  247.910004     49598100  \n",
              "\n",
              "[563 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b84f7b6f-e388-4fd9-8b25-223d2e6bce0c\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Date</th>\n",
              "      <th>Adj_Close_AAPL</th>\n",
              "      <th>Close_AAPL</th>\n",
              "      <th>High_AAPL</th>\n",
              "      <th>Low_AAPL</th>\n",
              "      <th>Open_AAPL</th>\n",
              "      <th>Volume_AAPL</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2024-01-02</td>\n",
              "      <td>183.731308</td>\n",
              "      <td>185.639999</td>\n",
              "      <td>188.440002</td>\n",
              "      <td>183.889999</td>\n",
              "      <td>187.149994</td>\n",
              "      <td>82488700</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2024-01-03</td>\n",
              "      <td>182.355591</td>\n",
              "      <td>184.250000</td>\n",
              "      <td>185.880005</td>\n",
              "      <td>183.429993</td>\n",
              "      <td>184.220001</td>\n",
              "      <td>58414500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2024-01-04</td>\n",
              "      <td>180.039658</td>\n",
              "      <td>181.910004</td>\n",
              "      <td>183.089996</td>\n",
              "      <td>180.880005</td>\n",
              "      <td>182.149994</td>\n",
              "      <td>71983600</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2024-01-05</td>\n",
              "      <td>179.317184</td>\n",
              "      <td>181.179993</td>\n",
              "      <td>182.759995</td>\n",
              "      <td>180.169998</td>\n",
              "      <td>181.990005</td>\n",
              "      <td>62379700</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2024-01-08</td>\n",
              "      <td>183.652130</td>\n",
              "      <td>185.559998</td>\n",
              "      <td>185.600006</td>\n",
              "      <td>181.500000</td>\n",
              "      <td>182.089996</td>\n",
              "      <td>59144500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>558</th>\n",
              "      <td>2026-03-25</td>\n",
              "      <td>252.619995</td>\n",
              "      <td>252.619995</td>\n",
              "      <td>255.000000</td>\n",
              "      <td>251.600006</td>\n",
              "      <td>254.100006</td>\n",
              "      <td>28476700</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>559</th>\n",
              "      <td>2026-03-26</td>\n",
              "      <td>252.889999</td>\n",
              "      <td>252.889999</td>\n",
              "      <td>257.000000</td>\n",
              "      <td>250.770004</td>\n",
              "      <td>252.119995</td>\n",
              "      <td>41796700</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>560</th>\n",
              "      <td>2026-03-27</td>\n",
              "      <td>248.800003</td>\n",
              "      <td>248.800003</td>\n",
              "      <td>255.490005</td>\n",
              "      <td>248.070007</td>\n",
              "      <td>253.899994</td>\n",
              "      <td>47900000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>561</th>\n",
              "      <td>2026-03-30</td>\n",
              "      <td>246.630005</td>\n",
              "      <td>246.630005</td>\n",
              "      <td>250.869995</td>\n",
              "      <td>245.509995</td>\n",
              "      <td>250.070007</td>\n",
              "      <td>39446200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>562</th>\n",
              "      <td>2026-03-31</td>\n",
              "      <td>253.789993</td>\n",
              "      <td>253.789993</td>\n",
              "      <td>255.479996</td>\n",
              "      <td>247.100006</td>\n",
              "      <td>247.910004</td>\n",
              "      <td>49598100</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>563 rows × 7 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b84f7b6f-e388-4fd9-8b25-223d2e6bce0c')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-b84f7b6f-e388-4fd9-8b25-223d2e6bce0c button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-b84f7b6f-e388-4fd9-8b25-223d2e6bce0c');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_6374b47c-3f9e-422d-80ed-b0491bbda98a\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_6374b47c-3f9e-422d-80ed-b0491bbda98a button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 563,\n  \"fields\": [\n    {\n      \"column\": \"Date\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"2024-01-02 00:00:00\",\n        \"max\": \"2026-03-31 00:00:00\",\n        \"num_unique_values\": 563,\n        \"samples\": [\n          \"2024-12-30 00:00:00\",\n          \"2026-01-30 00:00:00\",\n          \"2025-01-28 00:00:00\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Adj_Close_AAPL\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 30.510154349754803,\n        \"min\": 163.51190185546875,\n        \"max\": 285.9224548339844,\n        \"num_unique_values\": 556,\n        \"samples\": [\n          269.6260986328125,\n          221.31619262695312,\n          169.82444763183594\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Close_AAPL\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 30.133003759013636,\n        \"min\": 165.0,\n        \"max\": 286.19000244140625,\n        \"num_unique_values\": 547,\n        \"samples\": [\n          216.7899932861328,\n          166.89999389648438,\n          200.3000030517578\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"High_AAPL\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 30.34069642712312,\n        \"min\": 166.39999389648438,\n        \"max\": 288.6199951171875,\n        \"num_unique_values\": 547,\n        \"samples\": [\n          216.89999389648438,\n          169.3000030517578,\n          202.3000030517578\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Low_AAPL\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 29.91224729494832,\n        \"min\": 164.0800018310547,\n        \"max\": 283.29998779296875,\n        \"num_unique_values\": 549,\n        \"samples\": [\n          228.60000610351562,\n          169.17999267578125,\n          272.8399963378906\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Open_AAPL\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 30.178467203789754,\n        \"min\": 165.35000610351562,\n        \"max\": 286.20001220703125,\n        \"num_unique_values\": 543,\n        \"samples\": [\n          258.6600036621094,\n          272.1499938964844,\n          199.72999572753906\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Volume_AAPL\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 26413260,\n        \"min\": 17910600,\n        \"max\": 318679900,\n        \"num_unique_values\": 563,\n        \"samples\": [\n          35557500,\n          92443400,\n          75707600\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Una vez extraida la información, tenemos un DataFrame con las siguientes variables:\n",
        "\n",
        "+ `Date`: Fecha correspondiente a cada registro de la serie de tiempo.\n",
        "+ `Open_AAPL`: Precio de apertura de la acción al inicio de la jornada.\n",
        "+ `High_AAPL`: Precio máximo alcanzado por la acción durante el intervalo de tiempo seleccionado.\n",
        "+ `Low_AAPL`: Precio mínimo registrado durante el intervalo de tiempo seleccionado.\n",
        "+ `Close_AAPL`: Precio de cierre de la acción al final del intervalo de tiempo seleccionado.\n",
        "+ `Adj_Close_AAPL`: Precio de cierre ajustado, el cual incorpora efectos de dividendos y divisiones de acciones, proporcionando una medida más consistente para análisis históricos.\n",
        "+ `Volume_AAPL`: Número total de acciones negociadas durante el día (volumen de transacciones).\n",
        "\n",
        "En las series de tiempo `x` siempre es la variable temporal, en esta caso `Date`, mientras que `y` puede ser cualquiera de las restantes, dependiendo de lo que se esté analizando. En este caso recomiendo usar `Adj_Close_APPL` debido a que es la que incorpora más información.\n",
        "\n",
        "Primero se debe revisar el DataFrame para asegurarnos de que las variables son del tipo adecuado (sin variables tipo `object`)."
      ],
      "metadata": {
        "id": "N1AeaTEmuKR4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2KYmQmIBvxaN",
        "outputId": "75e0db97-4971-45ef-f293-73d6dd9433b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 563 entries, 0 to 562\n",
            "Data columns (total 7 columns):\n",
            " #   Column          Non-Null Count  Dtype         \n",
            "---  ------          --------------  -----         \n",
            " 0   Date            563 non-null    datetime64[ns]\n",
            " 1   Adj_Close_AAPL  563 non-null    float64       \n",
            " 2   Close_AAPL      563 non-null    float64       \n",
            " 3   High_AAPL       563 non-null    float64       \n",
            " 4   Low_AAPL        563 non-null    float64       \n",
            " 5   Open_AAPL       563 non-null    float64       \n",
            " 6   Volume_AAPL     563 non-null    int64         \n",
            "dtypes: datetime64[ns](1), float64(5), int64(1)\n",
            "memory usage: 30.9 KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ahora se declara `x` y `y`."
      ],
      "metadata": {
        "id": "FqYw8xXKwOfj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = df[\"Date\"]\n",
        "y = df['Adj_Close_AAPL']"
      ],
      "metadata": {
        "id": "JgOZDRPfsz4l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# @title\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# --- Configuración general del gráfico ---\n",
        "plt.figure(\n",
        "    figsize=(10, 5),   # tamaño de la figura (ancho, alto) en pulgadas\n",
        "    dpi=100           # resolución del gráfico\n",
        ")\n",
        "\n",
        "# --- Gráfico de línea ---\n",
        "plt.plot(\n",
        "    x, y,\n",
        "    color='black',   # color de la línea\n",
        "    linewidth=1.0,        # grosor de la línea\n",
        "    linestyle='-',        # estilo de línea\n",
        "    marker='o',           # marcador en cada punto\n",
        "    markersize=0,         # tamaño del marcador\n",
        "    markerfacecolor='white',\n",
        "    markeredgecolor='black',\n",
        "    label='Serie de tiempo'\n",
        ")\n",
        "\n",
        "# --- Título ---\n",
        "plt.title(\n",
        "    '',\n",
        "    fontsize=14,\n",
        "    fontweight='bold'\n",
        ")\n",
        "\n",
        "# --- Etiquetas de los ejes ---\n",
        "plt.xlabel(\n",
        "    'Fechas',\n",
        "    fontsize=12\n",
        ")\n",
        "\n",
        "plt.ylabel(\n",
        "    'Precios de cierre ajustados (Apple)',\n",
        "    fontsize=12\n",
        ")\n",
        "\n",
        "# --- Fuente de los ticks ---\n",
        "plt.xticks(fontsize=10)\n",
        "plt.yticks(fontsize=10)\n",
        "\n",
        "# --- Márgenes ---\n",
        "plt.margins(x=0.05, y=0.05)  # espacio extra alrededor de los datos\n",
        "plt.gca().spines['right'].set_visible(False) # derecha\n",
        "plt.gca().spines['top'].set_visible(False)   # superior\n",
        "\n",
        "# Para eliminar márgenes completamente, usar:\n",
        "# plt.margins(0)\n",
        "\n",
        "# --- Cuadrícula (opcional, pero didáctica) ---\n",
        "plt.grid(\n",
        "    visible=True,\n",
        "    linestyle='--',\n",
        "    linewidth=0.7,\n",
        "    alpha=0.8,\n",
        "    color=\"gray\"\n",
        ")\n",
        "\n",
        "# --- Leyenda ---\n",
        "plt.legend(\n",
        "    fontsize=10,\n",
        "    loc='best',\n",
        "    frameon=True\n",
        ")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 487
        },
        "id": "S_w4QIufwYYj",
        "outputId": "cb92cd80-a8fc-4190-a2c4-bddd33cbcffb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.legend.Legend at 0x7a63bf8c1a30>"
            ]
          },
          "metadata": {},
          "execution_count": 26
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x500 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1YAAAHECAYAAAA6bbsKAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQABAABJREFUeJzsnXdYFOf39u+l994RFVEUpSiKFbH33jX2mJhETTTFNJOY8ku3JDHGJF+NJXaNigULdkFsWMCIiNKU3nvfef/gnQkri+w+7LIMnM91cQnPzs4cbmeGveec5zwSjuM4EARBEARBEARBEMxoaToAgiAIgiAIgiAIsUPGiiAIgiAIgiAIooGQsSIIgiAIgiAIgmggZKwIgiAIgiAIgiAaCBkrgiAIgiAIgiCIBkLGiiAIgiAIgiAIooGQsSIIgiAIgiAIgmggZKwIgiAIgiAIgiAaCBkrOXAch/z8fNDayQRBEARBEARBKAIZKzkUFBTA3NwcBQUFmg4FDx8+1HQIooR0Y4e0Y4e0Y4e0Ux7SjB3Sjh3Sjh3STnnEphkZqyZOaGiopkMQJaQbO6QdO6QdO6Sd8pBm7JB27JB27JB2yiM2zchYEQRBEARBEARBNBAyVgRBEARBEARBEA1EwlGHhlrk5+fD3NwceXl5MDMz02gsmZmZsLGx0WgMYoR0Y4e0Y4e0Y4e0Ux7SjB3Sjh3Sjh3STnnEphllrJo4FRUVmg5BlJBu7JB27JB27JB2ykOasUPasUPasUPaKY/YNNPRdABiheM4VFZWoqqqSq3HOXfuHKZOnarWYzRHmqNu2tra0NHRgUQiUetxgoKCsGjRIrUeo7lC2rFD2ikPacYOaccOaccOaac8YtOMjBUD5eXlSElJQXFxsdqP1bFjR8TFxan9OM2N5qqbkZERHB0doaenp+lQCIIgCIIgiBqQsVISqVSKuLg4aGtrw8nJCXp6emrNIGRnZ8PKykpt+2+uNDfdOI5DeXk5MjIyEBcXhw4dOkBLiyp5CYIgCIIgmgpkrJSkvLwcUqkULi4uMDIyUvvxrKysYGBgoPbjNDeao26GhobQ1dVFQkICysvL1fb7DRw4UC37bQmQduyQdspDmrFD2rFD2rFD2imP2DSjR96MNFa2QFdXt1GO09xorro1xnnn6Oio9mM0V0g7dkg75SHN2CHt2CHt2CHtlEdsmpGxauJkZ2drOgRRQrqxs2fPHk2HIFpIO3ZIO+Uhzdgh7dgh7dgh7ZRHbJqRsSIazMCBA7FixQqV71cikeDIkSMq36+64iUIgiAIgiBaLmSsWggZGRl444030Lp1a+jr68PBwQEjRoxAaGhog/d96NAhfPXVVyqIUrVcvHgREokEubm5MuNNNV6CIAiCIAhCvFDziiaOqhpkTJkyBeXl5di+fTvatWuHtLQ0nDt3DllZWcz7LC8vh56eXpPsvvci3ZpivE2Jbt26aToE0ULasUPaKQ9pxg5pxw5pxw5ppzxi04wyVk0cY2PjBu8jNzcXV65cwffff49BgwahTZs26NmzJz766COMHz9eZrtXXnkFtra2MDMzw+DBg3Hv3j3h9c8//xxdu3bF5s2b4erqKnSle760rqysDO+99x6cnZ1hbGyMXr164eLFiy+MMSYmBgEBATAwMEDnzp0RHBxca5unT59i+vTpsLCwgJWVFSZMmID4+Hi5+8vIyMCgQYMAAJaWlpBIJFiwYAFTvNu2bYOFhQWOHz+Ojh07wsjICFOnTkVxcTG2b9+Otm3bwtLSEm+99ZbMgtFt27bFV199hVmzZsHY2BjOzs7YuHGjTJyJiYmYMGECTExMYGZmhunTpyMtLe2FWqkbX19fjR5fzJB27JB2ykOasUPasUPasUPaKY/YNCNj1cTJzMxs8D5MTExgYmKCI0eOoKysrM7tpk2bhvT0dJw8eRLh4eHw9fXFkCFDZBpBPH78GP/88w8OHTqEu3fvyt3PsmXLEBYWhr179yIiIgLTpk3DyJEjERMTI3d7qVSKyZMnQ09PD9evX8fvv/+ODz74QGabiooKjBgxAqamprhy5QpCQ0NhYmKCkSNHory8vNY+DQ0N8c8//wAAoqOjkZKSgp9//pk53uLiYvzyyy/Yu3cvTp06hYsXL2LSpEkICgpCUFAQ/v77b/zxxx84ePCgzL5//PFH+Pj44M6dO/jwww+xfPlywTRKpVJMmDAB2dnZuHTpEoKDgxEbG4sZM2bIjbOx2LFjh0aPL2ZIO3ZIO+Uhzdgh7dhpbto9e/YMFy5caJRjNTftGgOxaUalgCqguLgYDx8+VMu+c3JyYGlpKfe1Tp06KVQqqKOjg23btuHVV1/F77//Dl9fXwwYMAAzZ86Et7c3ACAkJAQ3btxAeno69PX1AQBr1qzBkSNHcPDgQSxevBhAdfnfjh07YGtrK/dYiYmJ2Lp1KxITE+Hk5AQAeO+993Dq1Cls3boV33zzTa33nD17Fg8fPsTp06eF93zzzTcYNWqUsM2+ffsglUqxefNmYUHmrVu3wsLCAhcvXsTw4cNl9qmlpSWU/NnZ2cHCwqJB8VZUVGDTpk1wc3MDAEydOhV///030tLSYGJigs6dO2PQoEG4cOGCjDHq168fPvzwQwCAu7s7QkNDsX79egwbNgznzp1DZGQk4uLi4OLiAqD6BtKlSxfcvHkTfn5+cmNWNxUVFRo5bnOAtGOHtFMe0owd0o6d5qbdzz//jK1bt6rkQXZ9NDftGgOxaUbGSgU8fPgQ3bt3b/Tj8lklRZgyZQrGjBmDK1eu4Nq1azh58iR++OEHbN68GQsWLMC9e/dQWFgIa2trmfeVlJTgyZMnws9t2rSp01QBQGRkJKqqquDu7i4zXlZWVmvfPFFRUXBxcRGMDQD06dNHZpt79+7h8ePHMDU1lRkvLS2ViU9ZFI3XyMhIMFUAYG9vj7Zt28LExERmLD09XWY/z/8effr0wU8//QTgv9+bN1UA0LlzZ1hYWCAqKkpjxoogCIIgWgrJycnIyspCVlZWnZ9TCEJRyFipgE6dOiE8PFwt+y4sLJT58P78cZXBwMAAw4YNw7Bhw/Dpp5/ilVdewerVq7FgwQIUFhbC0dFR7lyomtme+uZ8FRYWQltbG+Hh4dDW1pZ5ra7fQxEKCwvRvXt37Nq1q9Zr8owen3VTZL+KxPv8gsMSiUTumFQqVei4TZl27dppOgTRQtqxQ9opD2nGDmnHTnPTLiUlBUD1XG91G6vmpl1jIDbNyFipACMjI9FNrgOqsyP8OlG+vr5ITU2Fjo4O2rZty7zPbt26oaqqCunp6ejfv79C7/Hw8MDTp0+RkpIirLB97do1mW18fX2xb98+2NnZwczMrN59mpmZQU9PDwBkGkqoIl5leP73uHbtGjw8PAD893s/ffpUyFo9ePAAubm56Ny5s8pjURS+6QehPKQdO6Sd8pBm7JB27DQ37Woaq969e6v1WM1Nu8ZAbJpR84omzvNrMLGQlZWFwYMHY+fOnYiIiEBcXBwOHDiAH374ARMmTAAADB06FH369MHEiRNx5swZxMfH4+rVq1i1ahVu3bql8LHc3d0xe/ZszJs3D4cOHUJcXBxu3LiBb7/9FidOnJD7nqFDh8Ld3R3z58/HvXv3cOXKFaxatUpmm9mzZ8PGxgYTJkzAlStXEBcXh4sXL+Ktt97Cs2fPau0zNzcXbdq0gUQiwfHjx5GRkYHCwkKVxKsMoaGh+OGHH/Do0SNs3LgRBw4cwPLly4Xf28vLC7Nnz8bt27dx48YNzJs3DwMGDECPHj0afGxWAgMDNXZssUPasUPaKQ9pxg5px05z0443Vo8ePVL7sZqbdo2B2DQjY9XEUcWkPRMTE/Tq1Qvr169HQEAAPD098emnn+LVV1/Fr7/+CqC6jC0oKAgBAQFYuHAh3N3dMXPmTCQkJMDe3l6p423duhXz5s3Du+++i44dO2LixIm4efMmWrduLXd7LS0tHD58GCUlJejZsydeeeUVfP311zLbGBkZ4fLly2jdujUmT54MDw8PLFq0CKWlpXIzWBUVFXB2dsYXX3yBDz/8EPb29li2bJlK4lWGd999F7du3UK3bt3wf//3f1i3bh1GjBgBoFrzwMBAWFpaIiAgAEOHDkW7du2wb9++Bh+3ITTGBN7mCmnHDmmnPKQZO6QdO81Ju5KSEuTl5QGo7iCsbpqTdo2F2DSTcBzHaTqIpkZ+fj7Mzc2Rl5dX60N7aWkp4uLiZNZxUicZGRkvbBZByKcp6Na2bVusWLFCZs2shtIY59+WLVuwaNEitey7uUPasUPaKQ9pxg5px05z0i42NhZubm5wcXGBs7MzwsLC1Hq85qRdYyE2zShj1cTR0aFpcCyQbuxQVyR2SDt2SDvlIc3YIe3YaU7a8WWAPj4+tbr6qoPmpF1jITbNyFg1cepaw4p4MaQbOxMnTtR0CKKFtGOHtFMe0owd0o6d5qQdb6y6du3aKMaqOWnXWIhNMzJWTZyCggJNhyBKmoJu8fHxKi0DbCzktdwnFIO0Y4e0Ux7SjB3Sjp3mpF1UVBQsLS3RsWNHFBYWori4WK3Ha07aNRZi04yMVROntLRU0yGIEtKNnYYsuNzSIe3YIe2UhzRjh7Rjpzlpd+PGDfTs2VNo0qXurFVz0q6xEJtmZKwIgiAIgiCIFgXHcbh+/Tp69uwJOzs7AOo3VkTzh4wVI43VTFEikTTKcZobzVW3xjjvqPEHO6QdO6Sd8pBm7JB27DQX7RISEpCRkSGTsUpLS1PrMZuLdo2J2DRrUsbq22+/hZ+fH0xNTWFnZ4eJEyfWWlcgNTUVc+fOhYODA4yNjeHr64t//vlHZpvs7GzMnj0bZmZmsLCwwKJFi+QuDsuCrq4uAKi9DpfHxsamUY7T3GiuuvHnHX8eqoP58+erbd/NHdKOHdJOeUgzdkg7dpqLdtevXwcA9OzZU/jMoO6MVXPRrjERm2ZNygZeunQJS5cuhZ+fHyorK/Hxxx9j+PDhePDgAYyNjQEA8+bNQ25uLo4ePQobGxvs3r0b06dPFxZhBYDZs2cjJSUFwcHBqKiowMKFC7F48WLs3r27wTFqa2vDwsJCuPiMjIzUmh0pKSmBoaGh2vbfXGluunEch+LiYqSnp8PCwgLa2tpqO9adO3eEa4lQDtKOHdJOeUgzdkg7dpqLdjdu3EDbtm2FMkBra2u1G6vmol1jIjbNmpSxOnXqlMzP27Ztg52dHcLDwxEQEAAAuHr1KjZt2oSePXsCAD755BOsX78e4eHh6NatG6KionDq1CncvHkTPXr0AABs2LABo0ePxpo1a+Dk5NTgOB0cHAA0Ti1uYWEhTExM1H6c5kZz1c3CwkI4/9TF7du3RXUTa0qQduyQdspDmrFD2rHTXLS7ceMGevXqJfxsZ2en9lLA5qJdYyI2zZqUsXqevLw8AICVlZUw1rdvX+zbtw9jxoyBhYUF9u/fj9LSUgwcOBAAEBYWBgsLC8FUAcDQoUOhpaWF69evY9KkSbWOU1ZWhrKyMuHn/Pz8F8YlkUjg6OgIOzs7VFRUNORXrJeDBw9i6tSpaj1Gc6Q56qarq6vWTBVBEARBtAQqKioQHh4u85mwbdu2iI2N1WBURHOgyRorqVSKFStWoF+/fvD09BTG9+/fjxkzZsDa2ho6OjowMjLC4cOH0b59ewDVc7D4tC6Pjo4OrKyskJqaKvdY3377Lb744ota4zt27BDKyWbNmoWUlBSZfvqjR4+Grq4uAgMDhbF+/frBzc0NO3bsEMY8PT3Rq1cv7N27F0VFRQCAVq1aYcSIETh58iSSk5MBAGZmZpg2bRquXr2KqKgoANVZMT09PURFReHatWvCPidPnoyioiKcPn1aGBsyZAisra2xf/9+YaxHjx7w8fHB1q1bIZVKAQAdOnRAQEAADh8+jOzsbADVT2rGjRuHc+fOIT4+HgCgr6+POXPmIDw8HHfv3hX2+dJLLyEpKQmXLl0SxsaMGQNtbW0cPXpUGPP394erqyv+/vtvYczLyws9e/bEnj17hPlCrVu3xrBhw3DixAnh/8jc3BxTp05FSEiIzDy7RYsWITIyEjdu3BDGpk6divz8fJw5c0YYKysrQ3l5OQ4cOCCM+fn5wdvbG3/99ZfQBMLd3R39+/fHP//8g9zcXACAvb09xo4di7NnzyIhIQEAYGBggNmzZ+PmzZuIiIgQ9jlnzhwkJibi8uXLwtjYsWMBAMePHxfGAgIC0Lp1a+zcuVMY8/b2hp+fH3bt2iW0h2/Tpg2GDh2K48ePC0/OLCwsMGXKFFy5cgWPHj0CUG3uX375ZURERODmzZvCPqdNm4acnBycPXtWGBs+fDjMzMxw8OBBYaxnz57w8vLCli1bhLGOHTvC398fWVlZwriDgwPGjBmD4OBgJCYmAqguf501axZu3LiByMhI4f1z585FXFwcQkJChLHx48ejqqoKJ06cEMYGDBgAZ2dnmdLcrl27onv37ti5c6fwkKNt27YYMmQIjh07JmSHraysMGnSJFy+fBkxMTEAAC0tLSxcuBD37t3DrVu3hH1Onz4dWVlZOHfunDA2YsQIGBsb49ChQ8JY79694eHhga1btwpjHh4e6Nu3Lw4cOCA8aHFycsKoUaNw+vRpPHv2DABgbGyMmTNn4vr167h//z7S09OxZcsWzJs3D0+ePEFoaKiwzwkTJqCiogJBQUHC2MCBA+Ho6Ig9e/YIY926dYOvry927NghPLhp164dBg0ahMDAQGRmZgKoLluZOHEiLl68KLSj1dHRwfz583Hnzh3cvn1b2OfMmTORnp6O8+fPC2MjR46EoaEhDh8+LIz16dMHHTt2xLZt24Sxzp07o0+fPti3b58wV9XZ2RkjR47EqVOnkJSUBAAwMTHBjBkzEBYWhgcPHgjvX7BgAaKjoxEWFiaMTZo0CSUlJTJVCqWlpSgqKsLevXuFMV9fX3Tr1g3bt29HZWUlAMDNzQ0DBw7EkSNHkJWVBaB6TuWECRNw4cIF4YORrq4u5s2bh9u3b+POnTvCPjV1LweAhQsXqvRezp+bzflePnToUFhaWqr8Xl5YWChz/2uO9/KDBw8KD6hVeS/n73Nivpc7OjqipKRE+F2MjY3RqVMnHDx4UEZLVd/L+f+P5nwvHzx4MOzs7FR2L8/IyACAJnEvX7RoEepDwjVWezsleeONN3Dy5EmEhISgVatWwvibb76JGzdu4JtvvoGNjQ2OHDmC9evX48qVK/Dy8sI333yD7du312p6YWdnhy+++AJvvPFGrWPJy1i5uLggLy8PZmZm6vslFaCoqEiYX0YoDunGDmnHDmnHDmmnPKQZO6QdO81Buz///BNLlixBfn4+jIyMZMaKioqgr6+vluM2B+0aG7Fp1qS6AvIsW7YMx48fx4ULF2RM1ZMnT/Drr7/ir7/+wpAhQ+Dj44PVq1ejR48e2LhxI4DqpzLPz32qrKxEdnZ2nXNT9PX1YWZmJvPVVKA1Fdgg3dgh7dgh7dgh7ZSHNGOHtGOnOWh3/fp1eHt7C6YKADp16oSqqiq1LkjbHLRrbMSmWZMyVhzHYdmyZTh8+DDOnz8PV1dXmdf5cgMtLdmwtbW1hdKIPn36IDc3F+Hh4cLr58+fh1QqlZmkKBZqpnsJxSHd2CHt2CHt2CHtlIc0Y4e0Y6c5aHfjxg2hCRpPp06dAAAPHz4UxjIyMvD06VOVHbc5aNfYiE2zJmWsli5dip07d2L37t0wNTVFamoqUlNTUVJSAqD6pG/fvj1ee+013LhxA0+ePMHatWsRHByMiRMnAqiupx05ciReffVV3LhxA6GhoVi2bBlmzpypko6ABEEQBEEQhDiJjIzE/fv3MWjQIJlxW1tbtG7dGt98840wZ9Hf3x+tW7dGE501QzRBmpSx2rRpE/Ly8oRJgPzXvn37AFRPRg4KCoKtrS3GjRsHb29v7NixA9u3b8fo0aOF/ezatQudOnXCkCFDMHr0aPj7++PPP//U1K9FEARBEARBNAF++OEHtG7dGpMnT5YZl0gkOHr0KOLj4zF06FBkZWUJTUaMjIxw8uRJTYSrEu7fv4/Hjx9rOowWQZNtXqFJ8vPzYW5u3iSaVyQlJcHZ2VmjMYgR0o0d0o4d0o4d0k55SDN2SDt2xKxdQkIC3NzcsHbtWixfvlzuNpGRkRgyZAjMzMxk5ltNmTJFpiMjC5rSrl+/ftDX1xddWR0gvvOtybZbJ6rh270TykG6sUPasUPasUPaKQ9pxg5px46YtVu3bh3MzMxe2Dbby8sLJ06cEOZgnT9/Hrt27ZJZloAVTWkXExODnJwc5OfnazxhoCxiO9+aVCkgUZua6xIQikO6sUPasUPasUPaKQ9pxg5px45YtXv27Bn++OMPrFixAiYmJi/c1s/PT/i+X79+GDJkCB4/fiysPcWKJrQrKChARkYGKisrZdZFEwtiO9/IWBEEQRAEQRDNml9++QXGxsZYsWKFQtvfvHkT69evh56entBVuuaC1mKBL2fU09OTWdSYUA9krAiCIAiCIIhmzfHjxzFp0iSFS+F69OghmDBXV1fY2tri2rVraoxQ9Vy7dk1o7jZjxgycPHmSOhyqGTJWTZw+ffpoOgRRQrqxQ9qxQ9qxQ9opD2nGDmnHjhi1i4+PR1RUFEaNGsX0folEgl69euH69esNiqOxtduwYQNSUlIAAPPmzUNycjIiIiIaNYaGIrbzjYxVE6djx46aDkGUkG7skHbskHbskHbKQ5qxQ9qxI0btgoODoa2tjaFDhzLvgzdWUqmUeR+NrZ2Li4vwff/+/WFsbIygoCBERUXhhx9+aNRYWBHb+UbGqomzbds2TYcgSkg3dkg7dkg7dkg75SHN2CHt2Gkq2hUXFwsL+dbHzZs34enpCXNzc+bj9e7dG3l5ecLaViw0tnZFRUVwcXHB06dPoa+vj6FDh+LkyZPo27cvPvjgg0aNhZWmcr4pChkrgiAIgiAIQlSMGDEC1tbWCm178+ZN9OjRo0HH8/Pzg0QiEdU8q6KiIjg7O6NVq1YAgNGjR+Pq1avIzc3VbGDNGDJWBEEQBEEQhKgICQkBAFRUVLxwu5KSEty/f7/Bxsrc3BweHh4ICgrC1atXG7SvxqKoqAjGxsbCz6NGjUJVVZXwc0PKGgn5NNhYlZaWoqysTBWxEHLo3LmzpkMQJaQbO6QdO6QdO6Sd8pBm7JB27DQV7SwsLABUL377IiIiIlBZWdlgYwVUz7M6cOAA+vXrx/T+xtauuLhYxli5uLjA09NT+Lk+U8pz/PhxuLq6Kry9Kmkq55uiKG2sLl68iLfffhs9e/aEiYkJjI2NYWRkBFNTU/Ts2RMrVqzAxYsX1RBqy0Rs3VCaCqQbO6QdO6QdO6Sd8pBm7JB27DQV7fjGDP/+++8Lt7t16xb09PTg5eXV4GPWNCX5+fm1Xq+qqpLJCD1PY2v3fMYKgNB+HQDKy8sV2k9oaCji4+Nx584dlcanCE3lfFMUhYxVRUUFfv31V7Rr1w6DBw/G33//DQsLC8yZMwfvv/8+Vq5ciZdeegkWFhbYuXMnBg8eDFdXV/z6668acbfNiX379mk6BFFCurFD2rFD2rFD2ikPacYOacdOU9FOX18fgGLGytvbW9i+Ibz++ut4//33AQBJSUn45ptvEBoaKrz+ySefwMnJCUeOHMH58+cxc+ZMtG/fHqmpqQAaXzt5xmr27NnC94p+RuezgleuXFFdcArSVM43RdFRZKP27dujvLwc8+fPx/Tp0+Hr6/vC7cPDw3HgwAF88803WLNmDeLj41URa4uksLBQ0yGIEtKNHdKOHdKOHdJOeUgzdkg7dpqKdgUFBQCAc+fOYfXq1ZBIJHK3u3nzJvr376+SYxoZGeH111/HDz/8gMePH2P16tUYNmwYgoKCAABnzpxBSUkJJk2aBADw8PBAamoqfvvtN3z55ZeNrp08Y+Xt7Y1jx45h3LhxCmesHj9+DKB6Xtu7776r8jhfRFM53xRFoYzVxx9/jPj4eHz33Xf1mioA6N69O7777jvEx8fjo48+anCQBEEQBEEQBMFTUFAAPz8/hISE4OjRo3K3KSwsRFRUlErmV/E4OTkBAIKCglBZWYng4GDk5OSgpKQEERER+P777xEUFIQrV67g33//xcsvv4zff//9hSWC6kKesQIAXV1dAIqVAnIch8ePH8PAwACRkZEqj7G5oZCxeu2115hSqHp6enjttdeUfh/xH87OzpoOQZSQbuyQduyQduyQdspDmrFD2rHTVLQrKCjAjBkzMHz4cLz33ntyTcLdu3chlUpVaqz09fVhZ2eHI0eOQEdHB1VVVThy5Aju3LmDyspK9OrVC6NGjYK/vz8kEgmmTJmCjIwMREZGNrp2dRkrPT09AIqVAqakpKCoqAhdunRBcXGxymOsj6ZyvimKStqt5+XlacSJtwRGjhyp6RBECenGDmnHDmnHDmmnPKQZO6QdO01BO6lUisLCQpiZmWHdunV48uSJ3Lk4t27dgoGBgco7y7Vq1Qqpqanw8fFB//79ceDAAdy4cQP6+vq1mmT06tUL+vr6uHTpUqNrp4qMVWxsLACgS5cuKC0tVW2ACtAUzjdlYDZWt27dwsiRI2FkZARra2tcunQJAJCZmYkJEyZQZ0AVcerUKU2HIEpIN3ZIO3ZIO3ZIO+Uhzdgh7dhpCtoVFRWB4ziYmpqiS5cucHd3x61bt2ptd+vWLXTt2lUwEqqCz9yMHDkS06dPR3BwME6dOgVfX99axzIwMECvXr1w8eLFRtVOKpXWarfOo0zGKicnB0C1mSwpKVFtkArQFM43ZWAyVlevXoW/vz9iYmIwZ84cmQXGbGxskJeXhz/++ENlQbZkkpKSNB2CKCHd2CHt2CHt2CHtlIc0Y4e0Y6cpaMc3rjA1NQVQ3ZDh3r17tba7efOmSssAeZYuXYqxY8di9erVmDJlCqqqqnD69Gn07NlT7vaTJ0/G0aNHGzXpwJugFxkrRTJWvNZ2dnYoLS0Fx3EqjLJ+msL5pgxMxurjjz+Gh4cHHjx4gG+++abW64MGDcL169cbHBxBEARBEATRcjhz5ky9H6b5D/tmZmYAAB8fH9y7d0/mQ79UKkVMTAy6dOmi8hiXLVuGY8eOQVdXFw4ODggICABQXfZX1/Z9+vTB5s2bkZeXp/J45FFUVARAvrFSphSwoKAAWlpasLKyAgCNlAOKCSZjdfPmTSxcuBD6+vpy21s6OzsLPfuJhmFiYqLpEEQJ6cYOaccOaccOaac8pBk7pB076tROKpVi8uTJ+PLLL1+43fMZKx8fH+Tm5uLp06fCNoWFheA4DpaWlmqLl2f69OkAUGfGSltbGzt37kRxcTF++OEHtccDvNhYKVMKWFBQABMTExgZGQFofGMltmuVyVjp6urKlP89T1JSkuiEaKrMmDFD0yGIEtKNHdKOHdKOHdJOeUgzdkg7dtSpXWxsLIqKihAUFPTCkrP8/HwAsqWAABARESFsw2eGzM3N1RWuwCuvvILg4GC4ubnVuU3btm0xceJEnDt3Tu3xAKrNWJmamsLQ0BAAGn2eldiuVSZj1bt3bxw8eFDua0VFRdi6dSsGDBjQoMCIasLCwjQdgigh3dgh7dgh7dgh7ZSHNGOHtGNHndrxxujZs2dy50zxPJ+xcnFxgYWFhcx7eGPFlwuqEz09PQwdOrTe7ZydnREeHt4oi97yWqgiY2VqagoDAwMAjW+sxHatMhmrL774Ardu3cKYMWNw8uRJANX/gZs3b0b37t2RkZGBTz/9VKWBtlQePHig6RBECenGDmnHDmnHDmmnPKQZO6QdO+rULjIyElZWVnBycsIHH3wAjuMQFhaGAQMG4IMPPhC2e36OlUQiEeZZ8fBZrcbIWCmKqakpKisrce3aNbUe58GDB5gzZw4A1TSv0GTGSmzXKpOx6tWrF4KCgvD48WPMmzcPAPDuu+9i8eLFqKqqQlBQkJCWJQiCIAiCIIj6iIiIQNeuXbFlyxacOXMGv//+Oz744AM8evQIP/zwA/bu3QugOhulo6MDfX194b3PdwZszFJARXF0dIS1tTWuXLmi1uM8e/ZM+P5FpYDKZKw0ZazEhg7rGwcPHozo6GjcvXsXMTExkEqlcHNzQ/fu3eU2tCAIgiAIgiAIeeTm5uL06dNYuXIlRo4ciddffx3vvfceSktL8ccff2Dbtm04ePAgRo8ejfXr16Nnz54ynzd9fHzw66+/ori4GEZGRo1aCqgoWlpa8Pf3x+XLl9V6nPT0dADAO++8Azs7u1qvNyRjRV0BXwyzseLp2rUrunbtqoJQCHksWLBA0yGIEtKNHdKOHdKOHdJOeUgzdkg7dtShnVQqxXfffYfy8nIsXrwYAPDjjz/izJkziI2NxZgxYxAbG4u//voLr7/+OtLT03H69GmZffj4+IDjONy/fx++vr7Izs6GRCJpUs3UFixYgLy8PKxatQplZWUyGTdVkp6eDhMTE6xdu1bu68oaqzZt2mhsjpXYrlWFjBWrs+b7+hPsREdHo3PnzpoOQ3SQbuyQduyQduyQdspDmrFD2rGjDu1+//13fP/99/jkk0/g6OgIoLrN9qFDh3DhwgU4OjqiX79++Pbbb7Fnzx7s2bOnVge+Ll26QEtLC/fu3cPs2bPx+PFjmJubQ0uLadaLWoiOjkZAQABKS0sRHh6Ovn37quU46enpcjNVPNra2pBIJAqVAhYWFmq0FFBs16pCxmrgwIFKlfdxHAeJRIKqqirmwIhqwsLCRHVCNRVIN3ZIO3ZIO3ZIO+Uhzdgh7dhRh3bXr19Hr1698NVXX8mM+/j4wMfHBwDQt29f6OjoYOHChZg5c2atfRgaGsLd3R23bt3C48ePATSt+VVAtXbz58+HiYkJLl++rDFjBVRnrcTQvEJs16pCxurChQvqjoMgCIIgCIJogURHR6Njx44v3MbS0hIRERHo0KFDndv4+Pjgzz//FH5uSvOreHR0dNC3b19cvnwZH374oVqOoYix0tXVpeYVakAhY0VrUhEEQRAEQRCqhuM4REdHY/z48fVu6+Hh8cLXu3btin379gk/V1ZWNjg+dRAQEIAffvgBVVVV0NbWVvn+09PThUxfXSibsdLR0YGOjg41r6iHBjevSE9PR3x8PIDqVaXrc8iEckyaNEnTIYgS0o0d0o4d0o4d0k55SDN2SDt2VK1dZmYmcnNz4e7u3uB9LV68GEZGRiguLsZHH32ErKwsFUSoOnjt/Pz8kJ+fj4SEBLRr107lx1FVKWBVVRWKi4uFBiAGBgaNnrES27XKPKPv3Llz6NGjBxwdHdGnTx/06dMHjo6O6NGjB86ePavKGFs0lHJlg3Rjh7Rjh7Rjh7RTHtKMHdKOHVVrFx0dDQD1lgIqgpWVFd566y289tprANDkjBWvnY2NDYDqFvOqhuM4lZUCFhYWAqhe2BionsfW2NeO2K5VJmN1+PBhjBgxAikpKXj//fexefNmbN68GStXrkRKSgpGjRqFw4cPqzrWFsmpU6c0HYIoId3YIe3YIe3YIe2UhzRjh7RjR9XaPXr0CBKJBO3bt1fZPi0tLQFUt3FvSvDa8U011GGsioqKUFJSopKMVUJCAgDAwsICgGaMldiuVaZSwE8++QSenp64cuWK4GJ5Pv74Y/j7++OTTz4RXfqOIAiCIAiCaDyio6PRunVroTmCqpg8eTJGjhyp0n2qCt6oqMNY8YsDqyJj9dlnn6F169bo378/gGpjRXOsXgyTsYqNjcV3331Xy1QB1R1YFi1ahI8++qjBwREEQRAEQRDNF0U6ArLwzz//qHyfqoLPWOXl5al83xkZGQDqN1b1ZawuXLiAwMBA7N69WzC9mshYiQ2mUsBOnToJjlgeaWlpKpmESACDBw/WdAiihHRjh7Rjh7Rjh7RTHtKMHdKOHVVr9+jRI7UYq6YIr52Ojg5MTEw0mrF6kbGqqqrCO++8g969e8usGaaJ5hViu1aZjNUPP/yA33//HYGBgbVeO3z4MP744w+sWbOmwcER9V8YhHxIN3ZIO3ZIO3ZIO+Uhzdgh7dhRpXaVlZV4/Phxi3kYX1M7c3NztRkriUQCa2vrF273olLAHTt24O7du1i3bh0kEokwzmesAgMDMWjQIDx8+FClsctDbNcqk7HasGEDbG1tMXnyZLi4uGDQoEEYNGgQXFxcMHXqVNjZ2eGXX37B+PHjha8JEyaoOvYWwd69ezUdgigh3dgh7dgh7dgh7ZSHNGOHtGNHldolJCSgoqKixWSsampnYWGhNmNlbW0NHZ0Xz/aRl7G6cOECXn75Zezfvx/Dhg1Dnz59ZF43NDTEoUOHMHHiRFy6dAnbtm1Tdfi1ENu1yjTHKiIiAhKJBK1btwYAYR0rHR0dtG7dGqWlpYiMjJR5T03HSxAEQRAEQbRsVNlqXWxYWFioZY6VIq3WgdoZq8LCQqHsztvbG7169ar1Hjc3Nzx48ADr16/HsWPHcOTIEXz33XeqC74ZwGSseCNFEARBEARBECxER0fD0NAQrVq10nQojY46M1a2trb1bvd8xurMmTPC948ePcLo0aNrveeXX37BL7/8AgDQ0tLCX3/9hZiYGHTo0EEFkTcPmBcIJhoHX19fTYcgSkg3dkg7dkg7dkg75SHN2CHt2FGldo8ePUKHDh2gpdUyPo7W1E6dc6wUyVg9b6wePXokfF9aWiosYlwXAwcOhJaWFi5evMgcqyKI7Vpt0Jl8/PhxLFmyBKNHj8bo0aOxZMkSHD9+XFWxEQC6deum6RBECenGDmnHDmnHDmmnPKQZO6QdO6rUTl2t1psqNbVTZ8aKpRTw0aNHMpmu+ppfmJmZoVu3brh06RJ7sAogtmuVyVjl5uZi0KBBmDBhAjZv3ox///0X//77LzZv3owJEyZg4MCBajlZWiLbt2/XdAiihHRjh7Rjh7Rjh7RTHtKMHdKOHVVqFx0d3WI6AgKy2ml6jpW8jFXfvn2Fn+szVgAwYMAAXLp0CRzHsQWrAGK7VpmM1fLly3HlyhV8//33yMnJQUJCAhISEpCTk4PvvvsOISEhWL58uapjbZFUVlZqOgRRQrqxQ9qxQ9qxQ9opD2nGDmnHTkO1++abb/D111+jqKgIycnJLcpY1dROHRkrqVSKjIwMhY3V8xkrX19f6OnpAVDMWPXq1QvPnj1DdnY2e9D1ILZrlal5xZEjR7BkyRK89957MuPGxsZYuXIlEhMTsWPHDpUESBAEQRAEQYifR48eYdWqVQCA6dOnAwBcXFw0GZLGsLGxQW5uLkpLS2FgYKCSfebk5KCqqkrhUkA+Y5WTk4OMjAx07NgRtra2SEpKqneOFQC0b98eABAbG6uQEWsJMGWsdHV1X1gT26lTJ+jq6jIHRfyHm5ubpkMQJaQbO6QdO6QdO6Sd8pBm7JB27DREu7///hsA4OTkhLS0NACAg4ODSuISAzW14zvpPXnyRGX7T09PB6DYorr6+vooKysDAMTExAAA3N3dBUOliFHifx9V/g51HUMsMBmrKVOm4MCBA6iqqqr1WmVlJfbv349p06Ypvd9vv/0Wfn5+MDU1hZ2dHSZOnCiscVCTsLAwDB48GMbGxjAzM0NAQABKSkqE17OzszF79myYmZnBwsICixYtQmFhodLxNAUGDhyo6RBECenGDmnHDmnHDmmnPKQZO6QdOw3RLjk5GQBQUlKC1NRUAC3LWNXUji+BrNmNr6EoY6xMTExQUFAgE0OHDh1ga2sLiUQCCwuLevdhbm4OKysrxMbGsgddD2K7VpmM1Zw5c5CTk4O+fftiy5YtuHTpEi5duoTNmzejb9++yMvLw+zZs3H79m2Zr/q4dOkSli5dimvXriE4OBgVFRUYPnw4ioqKhG3CwsIwcuRIDB8+HDdu3MDNmzexbNkymVads2fPxr///ovg4GAcP34cly9fxuLFi1l+VY1z5MgRTYcgSkg3dkg7dkg7dkg75SHN2CHt2GmIdnyWKjc3F8nJydDT01PoA3xzoaZ2tra2MDc3r2WsHj9+jM8++4ypIYQyxsrU1FTGWDk5OcHExAQ2NjawtLSEtra2Qsd0c3OTyVhlZWVhypQpWL58uUqaWojtWmWaYzVgwADh+5s3b0IikQCAjIA1t+E4DhKJRG6GqyanTp2S+Xnbtm2ws7NDeHg4AgICAABvv/023nrrLXz44YfCdjXLEqOionDq1CncvHkTPXr0AABs2LABo0ePxpo1a+Dk5KTsr6tRsrKyNB2CKCHd2CHt2CHt2CHtlIc0Y4e0Y6ch2qWlpcHKygrZ2dmIjo6Gg4OD8BmyJVBTO4lEAnd391rG6rvvvsOWLVswa9YseHh4KLX/9PR06OrqwtzcvN5tnzdWfAbN0dFRqSxiu3btZIzVvn37cOjQIQDA559/DktLS2V+hVqI7VplMlZbt25VdRxy4dtQWllZAag+Ya5fv47Zs2ejb9++ePLkCTp16oSvv/4a/v7+AKozWhYWFoKpAoChQ4dCS0sL169fx6RJk2odp6ysTKgzBYD8/Hx1/loEQRAEQRAtjtTUVHh4eCA0NBRRUVEtqgxQHu7u7jJTXoqKirB//34AwJkzZ5iMlZ2dnUJm1dTUFOXl5SgvL8ejR4/g5+cHAPjwww+xaNEihY/p5uaGq1evCj8fPnxY+D4vL6/BxkpsMBmr+fPnqzqOWkilUqxYsQL9+vWDp6cnAAg1nJ9//jnWrFmDrl27YseOHRgyZAju37+PDh06IDU1tVYKVEdHB1ZWVkI97/N8++23+OKLL2qN79ixA4aGhgCAWbNmISUlRWaF6dGjR0NXVxeBgYHCWL9+/eDm5ibTFdHT0xO9evXC3r17hbLGVq1aYcSIETh58qRQc2xmZoZp06bh6tWriIqKAlA9X0wqlSIqKgrXrl0T9jl58mQUFRXh9OnTwtiQIUNgbW0tXJQA0KNHD/j4+GDr1q2QSqUAqmtoAwICcPjwYaFFpp2dHcaNG4dz584hPj4eQPXExjlz5iA8PBx3794V9vnSSy8hKSlJZlG4MWPGQFtbG0ePHhXG/P394erqKkxWBQAvLy/07NkTe/bsQXFxMQCgdevWGDZsGE6cOCH8H5mbm2Pq1KkICQmRueksWrQIkZGRuHHjhjA2depU5Ofn48yZM8KYgYEB8vPzceDAAWHMz88P3t7e+Ouvv4Tsqru7O/r3749//vlHaHtqb2+PsWPH4uzZs0hISBD2N3v2bNy8eRMRERHCPufMmYPExERcvnxZGBs7diwAyCyWHRAQgNatW2Pnzp3CmLe3N/z8/LBr1y6UlpYCANq0aYOhQ4fi+PHjQsmEhYUFpkyZgitXrghPtiQSCV5++WVERETg5s2bwj6nTZuGnJwcnD17VhgbPnw4zMzMcPDgQWGsZ8+e8PLywpYtW4Sxjh07wt/fH4WFhcK4g4MDxowZg+DgYCQmJgIAjIyMMGvWLNy4cQORkZHC++fOnYu4uDiEhIQIY+PHj0dVVRVOnDghjA0YMADOzs7YvXu3MNa1a1d0794dO3fuFB5ytG3bFkOGDMGxY8eE8gYrKytMmjQJly9fFibbamlpYeHChbh37x5u3bol7HP69OnIysrCuXPnhLERI0bA2NhYeJoGAL1794aHh4fMAyMPDw/07dsXBw4cEB60ODk5YdSoUTh9+jSePXsGoLoT6syZM3H9+nXcv38f2dnZ2LJlC+bNm4cnT54gNDRU2OeECRNQUVGBoKAgYWzgwIFwdHTEnj17hLFu3brB19cXO3bsEFrhtmvXDoMGDUJgYCAyMzMBVE8snjhxIi5evCg8LdTR0cH8+fNx584dmfLrmTNnIj09HefPnxfGRo4cCUNDQ5k/gn369EHHjh2xbds2Yaxz587o06cP9u3bJ8xVdXZ2xsiRI3Hq1CkkJSUBqK7XnzFjBsLCwvDgwQPh/QsWLEB0dDTCwsKEsUmTJqGkpESmSkFfXx9FRUXYu3evMObr64tu3bph+/btQstdNzc3DBw4EEeOHBGeZNrY2GDChAm4cOGC8HdCV1cX8+bNw+3bt3Hnzh1hn5q6lwPAwoULVXov5zVpzvfyoUOHwtLSUuX3cgAy97/meC8/ePCg8IBalfdy/j6n7L386NGjSE1NRbt27QAADx48gJubmxB7U7qX86j6Xs7/y9/LS0pKEB4ejsrKSpw/fx4rV65ESUkJnJyccPr0aQQEBCh1L7906RK0tbXx4MGDeu/l4eHhAKqTCVFRUWjfvj22bNmi9L3cxMQEycnJ+N///ofi4mJcvHgRs2fPxq5du7Bt2za4uLg06F7OX89N4V6ukOHkVExKSgq3fv16rkePHg3az+uvv861adOGe/r0qTAWGhrKAeA++ugjmW29vLy4Dz/8kOM4jvv66685d3f3WvuztbXlfvvtN7nHKi0t5fLy8oSvp0+fcgC4vLy8Bv0OBEEQBEEQBMdlZ2dzALh169ZxADgA3KuvvqrpsDTK5cuXOQBcSEgIN3z4cM7AwIA7ffo093//93+cubk5J5VKldrf5MmTuREjRii07ZkzZzgAwmfro0ePsvwKXGBgIAeAS0lJ4TZs2MDp6OgIv9eVK1eY9ilmmJpXPE9hYSG2b9+O4cOHw8XFBe+8806DFgtbtmwZjh8/jgsXLqBVq1bCuKOjI4Bq110TDw8P4QmMg4OD8HSbp7KyEtnZ2XWmnPX19WFmZibz1VS4cOGCpkMQJaQbO6QdO6QdO6Sd8pBm7JB27LBqx2fuapa3tbRSwOe148vv/P39ERISgqCgIAwfPhxeXl7Iy8sTMieK8vTpU4U1NTU1BQAhc8W6ULOzszMAICkpCdu2bcOYMWOEFul8xrQhiO1aZTZWlZWVOHr0KGbMmAF7e3u8/PLLSE9Px5dffonIyEimnvYcx2HZsmU4fPgwzp8/D1dXV5nX27ZtCycnp1ot2B89eoQ2bdoAqC5lyc3NFU4UADh//jykUil69erF8JtqFnW2sGzOkG7skHbskHbskHbKQ5qxQ9qxw6odXx7KlwICtR+UN3ee187AwAC2trYAgKCgIAwaNAgAhCkwNcsS66OwsBC3b99G7969FdrexMQEQLWx0tbWlvl/UQbeWJ0+fRrh4eFYsGCB0DxDFT0LxHatKj3H6sqVK9i1axcOHjyI7OxsdO/eHUuWLMHatWvx2WefYfLkyczBLF26FLt370ZgYCBMTU1larQNDQ0hkUiwcuVKrF69Gj4+PujatSu2b9+Ohw8fCjXHHh4eGDlyJF599VX8/vvvqKiowLJlyzBz5kzRdQQkCIIgCIJoDshbEHjIkCGaCqfJcP78eZSVlaF79+7CWNu2bWFsbIz79+9jxIgRCu0nNDQUVVVVgjmrj5oZq3bt2kFXV1f54FE9r1NHRwc//fQTrK2thXlOWlpaKslYiQ2FjdVHH32EPXv2IDExER4eHlixYgVmzpyJ9u3b48mTJ1i7dm2Dg9m0aROA2ouBbd26FQsWLAAArFixAqWlpXj77beRnZ0NHx8fBAcHy6zMvGvXLixbtgxDhgyBlpYWpkyZgl9++aXB8WkC1hO9pUO6sUPasUPasUPaKQ9pxg5pxw6rdmlpaTAwMBA+0AMQsjUtBXna8dmpmmhpaaFLly4KZawSEhKwbt06GBgYwMHBQeGSPv7/4cGDBxg1apRC75GHlpYWnJyckJiYiDfffBN6enoAqhs/qCJjJbZrVcJxiq3epaWlBVdXV/z1118ya1QBwJMnT9ChQwccPHiwQRmrpkJ+fj7Mzc2Rl5fXpOZbEQRBiJ2DBw/Cy8tLZv1BgiDExZMnT9CuXTuhrffdu3dhZ2f3wsqgVatWYdeuXYiPj8e7774LBwcHrFy5srFCFh3yOhLK448//sDrr7+Odu3awcvLS+EFdSsqKgQT9Pbbb2PdunXMsfbt2xdhYWEIDw+Hr68vgOqs25w5c/B///d/zPsVIwrPsZo6dSpSUlIwYsQIjB8/Hnv27BFaFBLqo2abTUJxSDd2SDt2SLsXc/LkSUybNk2oTqgJaac8pBk7pB07u3btQvv27fHdd98JY926dUNAQMAL35eamiqUAa5du7ZFmiplzjsXFxc8ffq03u34JS9iY2PRpUsXhfevq6sLfX19AOyNK3jatWsHb29vdOvWTRgzMzNTSSmg2K5VhY3V/v37kZaWhk2bNqGkpARz586Fvb09Zs6ciRMnTrSolbMbk5o9+wnFId3YIe3YIe3qJjk5GfPmzQOAWp1bAdKOBdKMHdKOHX49s9WrVyMyMlJYg6i+JgNpaWmwt7dXe3xNGWXOOxcXFyQnJ6OqquqF2/HGCoDSCwrz5YANNVbr16/HyZMnZbyAubm5SkoBxXatKtUV0NTUFAsXLkRwcDCePn2KL774AjExMVixYgU4jsNvv/2G3bt3C4t5EQRBEAQA/Pjjj5BIJBg8eLAwiZ0gCHHBcRxu3bqFhQsXwt3dHfPmzRMWeXZxcXnhe8lYKYeLiwuqqqqERm51UdNYKdtlUVXGytbWtlYZqKrmWIkN5nbrjo6OePfddxEeHo4HDx7go48+QmxsLObMmQM7OzuFu5IQBEEQzZ+4uDj4+fmhS5cucjNWBEE0HaRSKSQSiZCd4klJSUFWVhbGjx+PHTt24P79+xg9ejQAwNLS8oX7TE1NJWOlBLxRra8ckDdWEokEnTp1UuoYpqamMDIyUkvXbFWVAooNlSwQ3KlTJ3z99deIjY3F5cuXsWjRIqV67xN1M2vWLE2HIEpIN3ZIO3ZIu7pJSkqCk5MT7Ozs5GasSDvlIc3YIe1eDF959PHHH8uMR0REAAB8fHzg6+uLb775RngtJyenzv1xHIf09PQWtyDw8yhz3rVq1QqAYsaqb9++mD59OoyMjJSKx9TUFB06dICWlkrsgAyqKgUU27WqciX9/f2xadMmpKSkqHrXLRLSkQ3SjR3Sjh3Srm6Sk5Ph7OwMe3t7ZGZmorKyUuZ10k55SDN2SDv5HDt2DOvXrxdM0rNnz2Rej4iIgLGxMdq0aQMAWLlyJc6fP485c+YIc63kkZubi/Ly8hafsVLmvLO0tISRkdELjVVJSQlycnLw2muvYe/evUrH4+bmpvCCwsqiqoyV2K5VhYxVWFiY0jvW0dFhfi/xHxcvXtR0CKKEdGOHtGOHtJMPP0/AyckJ9vb24Diu1ocw0k55SDN2SDv5jB8/Hu+8845M9qm8vFz4PiIiAg4ODjIZjkGDBmHYsGEoKipCaWmp3P3yWeqWbqyUOe8kEkm9nQH5MkBnZ2emeLZu3YqNGzcyvbc+VJWxEtu1qpCxGjx4MAYNGoT9+/ejuLi43u0LCwuxe/duBAQE0KraBEEQLZy0tDRIpVKhFJAfIwiiafLw4UPh+8DAQOH78PBwoUStJjY2NgBQZ9aKb8DQ0ksBlaVt27aIi4ur83U+oyjv/0QRtLS0oK2tzfTe+mipzSt0FNno0aNH+PLLLzF37lzo6uqiV69e8PX1haurKywtLcFxHHJychAXF4dbt27hxo0bqKysxLx587Br1y51/w4EQRBEEyY5ORlA9VNVCwsLAPJbrhMEoVmMjIxQXFyMS5cuAQCGDBmCBQsWoG3bttDX18fDhw8xdOjQWu+ztrYGUG2s5GVPKGPFhpubGy5fvlzn6/Hx8QAglGY2JczMzFBaWory8nJhIeKWgELGysXFBf/73//w7bff4u+//0ZgYCB+++03lJSUyGxnaGiIHj164P/+7/8wd+5c2NraqiXolgTfbYdQDtKNHdKOHdJOPny5ipOTE0xMTACgVgth0k55SDN2SDv5mJiYCMZKS0sLgYGBGDp0KMaOHYv+/fvDxsYG7733Xq331TRW8khLS4OBgYHQ3ruloux55+bmhm3btoHjOLnrxSYkJMDBwQEGBgaqClFlmJubAwDy8/NhY2OD5ORkjBs3DqdOnVLKH4jtWlWqeYWNjQ3efvttXLx4EXl5eXj8+DGuX7+O69ev4/Hjx8jLy8OlS5fwzjvvkKlSEbq6upoOQZSQbuyQduyQdrXhOA6XL1+Gjo4ObG1tYWxsjLZt2wpr3/CQdspDmrFD2tVGKpUKxigmJgbm5uYwNjbG0aNHYWZmhn/++QerVq2CsbFxrfcqYqzs7e3lmoOWhLLnnZubG4qLi+tcyyo+Pr5JZquA6owVAKGBxebNm3H79m0hG1ofGRkZWLx4MRISEtQWozpg7gqoo6ODdu3awc/PD35+fmjXrp3QsIJQHTVrmwnFId3YIe3YIe1kqaysxLJly7Bu3TqsWrVKmPA+dOhQnD17VmZb0k55SDN2SLva5ObmoqqqSvhAzK9LZWtriytXruDOnTtYsWKFXO3Mzc2hpaWFzMxMuftOTU2l+VVQ/rxzc3MDADx58kTu6wkJCU3eWPHzrB4/fgwACs/pysjIwP/+9z/RXauqb1xPEARBtHg4jsP06dPxxx9/4M8//8Tnn38uvDZs2DBERUXVauVMEITm4Oc99uvXD4Dsgr8ODg7o2rVrne/V0tKCsbExioqK5L7OZ6wI5WjXrh2AFxurtm3bNmJEilOzFBAAoqOjAQDZ2dkKvZ8/l8Q2P4uMFUEQBKFyCgoKcPjwYfz000949dVXZV4bPHgwJBIJzp07p6HoCIJ4Ht5Y9e3bF0D1wxFlMDQ0rDX3noeMFRtGRkZwdHSUa6yqqqqQmJjY5DNWeXl5KCsrw7179wDIN1ZVVVWYMWMGevXqJYzxXcj19fUbIVrVQcaqicM/OSKUg3Rjh7Rjh7T7j9zcXACAu7t7rddsbGzQrVs3BAcHC2OknfKQZuyQdrV53ljVNV+qLu0MDQ3rXMcqNTWVjBXYzjs3Nze5xiolJQWVlZVN1ljVzFgFBwejrKwMgHxjtX//fuzfv1/oKg78l7Hy9/dvpIhVA02KauLw9bWEcpBu7JB27JB2wL59+/D06VMMGzYMAIT26s8zbNgwmW5XpJ3ykGbskHa1SU9Ph46ODrp37w6gbmNVl3Z1Zaw4jkN6ejrNsQLbeefm5iaU0dWEb7XeVEsB9fX1oauri7y8PJw5cwadO3eGkZGRXGN1+PBh4fvc3FzY2NgIxqpz586NFrMqoIxVE2fHjh2aDkGUkG7skHbskHbAzJkzsXLlSiFjVXOeRk2GDh2KtLQ03L9/HwBpxwJpxg5pV5v09HTY2dkJmQZ52Wagbu0MDAzkGqvc3FyUl5dTxgps511dGSu+W15TzVhJJBKYmZkhIyMDgYGBmD59OqysrGoZq8zMTJw6dQrDhw8H8J+h543VP//807iBNxCVGqvY2FhERUWpcpcEQRCECMnJyQFQd8bK398fBgYGtboDEgShGXhjBQC3b9/GqVOnlHp/XRkr/l5gZWXV8CBbIG5ubsjIyEBBQYHMeEJCAqytrYW1AZsi5ubmOHDgAPLz8zFt2rRaxqq4uBheXl4AgKVLlwKQNVa6urqi6zjOZKx++eUXzJw5U2Zs4cKF6NChAzw9PdGjRw+hVpcgCIJoefAZq7qMlYGBAfz9/WXmWREEoTlqGqtu3bopvR5pXcaqvnsB8WLq6gzYlNew4jEzM8ODBw/QpUsXdO7cuZaxunr1KlJTU3Hx4kX07NkTwH/Gqri4WO6aaU0dJmO1efNmmZTu6dOnsX37dixevBgbNmxAbGwsvvjiC5UF2ZLx9PTUdAiihHRjh7Rjp6Vrxy8ECVQ/pTY2Nn7hgphDhw7F5cuXUVVV1eK1Y4E0Y4e0q01NY/Ui6tKuruYVZKz+g+W8q2stq6a8hhUPX1Y6ffp0AKhlrM6fPw9bW1t069ZNyGjWzFgZGxuL7lplyq8lJCTAw8ND+Hn//v1wdXXFpk2bAFR3f/n7779VE2ELp2brSUJxSDd2SDt2Wrp2fM0/ACQnJ9f7QcrX1xdFRUWIi4tr8dqxQJqxQ9rVJiMjA35+fvVuV5d2hoaGwppFNSFj9R8s552NjQ1MTU3lZqzGjBmjqtDUAt9yfdq0aQDkGyt++Q09PT2YmpoKr/PGSmzXKlPG6vm1Dc6cOYNRo0YJP7dt2xapqakNi4wAAOzdu1fTIYgS0o0d0o6dlq5dTWOVkJBQZ+MKni5dugAA/v333xavHQukGTukXW3S09MVKv+rS7sXNa8A/vuQ3ZJhOe/4rqk1jRXHcU16DSsee3t7eHt7C8kYKysrFBYWory8HHl5ebh58yYGDx4sbG9lZSWTsTIyMhLdtcpkrNzd3YXWiKdPn0ZycrKMsXr27Bk9mVARda1iTrwY0o0d0o6dlq5dbGys8H1CQkK9fwccHR1haWmJ+/fvt3jtWCDN2CHtZKmoqEB2drZCpYB1afeiOVampqaia0KgDljPu+eNVXp6OkpLS5tsq3We77//XqYJCl/WeOfOHVy5cgVSqVTGWFlbW9eaYyW2a5XpLH/vvffw0ksvwdLSEkVFRfDw8MCIESOE18+fP4+uXbuqKkaCIAhCBJw9exampqYoKChAQkKCMBm5LiQSCTw9PfHvv//SGjcEoUEyMzMBQCFjVRcvMlb0sL1huLm5Yf/+/cLP/BpWTT1j9XwnyN69e8Pa2hqBgYEoLS2Fi4uLzNpeNY0VXwooNpiM1cyZM2FtbY2goCBYWFhgyZIlwpOI7OxsWFlZYe7cuSoNtKXSqlUrTYcgSkg3dkg7dlqydoWFhQgODsarr76KX3/9FWlpaQp9mOrcuTOuXbuG+fPnqz/IZkZLPt8aCmknC9/JWRFjVZd28ppXnD17FlevXiVj9f9hPe/c3NyQmJiI8vJy6OnpNfk1rOpCR0cHY8eORWBgIHR1dYX5VTzW1tZIS0sD8J+xEtu1yryO1bBhw7B+/XqsXr1apibXysoKhw4dwqRJk1QSYEunZiaQUBzSjR3Sjp2WrN2ZM2dQVlaGefPmCWP1zbECABcXFyQnJ7do7Vghzdgh7WRRxljVpZ28jNXLL7+Mc+fOkbH6/7Ced25ubpBKpUhMTARQnbEyMzMTpa4TJ07EgwcPcO/ePZkyQKD678GDBw9QUVEhzLES27XaoAWCi4qKEBQUhE2bNmHTpk0ICgoSXS1kU+fkyZOaDkGUkG7skHbstGTtjhw5Ak9PT5kycGtr63rfZ29vj8zMTBw/flyN0TVPWvL51lBIO1l4Y6VI84q6tHu+eUVWVhaePn0KgDoC8rCedzVbrj99+hSnT59GmzZtZLI9YmHYsGEwMDAAAAwaNEjmtXnz5iEtLQ1HjhwR5liJ7VplNlYbNmyAk5MTxo0bh6VLl2Lp0qUYO3YsnJyc8Ouvv6oyxhZNcnKypkMQJaQbO6QdOy1Vu4qKChw/fhwTJ06UWbeqc+fO9b7XwcEBHMchOjpanSE2S1rq+aYKSDtZ0tPTYWxsrNCclrq0ez5jdefOHeF76ghYDet55+LiAl1dXTx58gT9+/fH+fPnoaXVoNyIxjA2Nsbw4cPh7u4OFxcXmdc8PT0REBCAjRs3CqWAYrtWmeZY7dixA8uXL0efPn3w1ltvCW0Uo6KisGHDBixfvhzm5uY0z4ogCKIFcOXKFeTk5GDixIky415eXvW+l19sXt76NwRBNA4ZGRkKZateBD/HiuM4SCQSGWNVUFDQ0BBbNNra2mjbti12796NhIQEaGtrY/HixZoOi5nffvutznv+kiVLMHPmTBgYGLSc5hXr1q1DQEAAzp07B21tbWHc29sbU6dOxZAhQ7B27VoyViqAnvKwQbqxQ9qx01K1O3LkCFq1agVfX1+Z8ZrdnuqC7wZYWVmpltiaMy31fFMFpJ0s6enpCncErEs7Q0NDAEBZWRlCQ0OxZs0atG3bFvHx8UhJSVFZrGKmIeedm5sbTp06hTZt2uDJkycyn7/FhrOzM5ydneW+NmnSJNjb2yMtLQ3Gxsaiu1aZ8ojR0dGYNm2a3P9UbW1tTJs2jco6VAS/WjWhHKQbO6QdOy1Ru4yMDBw+fBgTJkyoVe+vyLo1/Ie5Dh06qCW+5kxLPN9UBWknizLGqi7teGNVUlKCTz75BC4uLjhz5gwA1Hro0lJpyHnHr1k1depUUZuq+tDT0xOycUZGRqK7VpmMlbm5udBDXx58txKi4Vy9elXTIYgS0o0d0o6dlqRdeHg4zp49iwEDBqCgoACvvPKK8Jq3t3etScl1oa+vD0tLS9y4cUNdoTZbWtL5pmpIO1mUMVZ1acc3JLhz5w6uXbuGDz74AB06dEBCQgJ+/vlnlcUqZhpy3pWXlwNAi+i6vXjxYujq6sLW1lZ01yqTsRozZgw2bNiAvXv31npt3759+PXXXzFu3LgGB0dUz1sjlId0Y4e0Y6claffOO+9gxowZiIqKwpYtW2S6Ad67dw/nz59XeF8ODg6IiYlRQ5Tqpby8HHv27NHY/3tLOt9UDWknizLGqi7t+IzVpk2bYGVlhfHjxwMAWrduDX19fdUEKnIact599NFHePPNN9G7d28VRtQ0adWqFaKjozF16lTRXatMc6y+++47hIWFYfbs2Xj33XeFEo6YmBikpqaiU6dO+O6771QaKEEQBNE0yM7ORmhoKKqqqgAAPXv2bND+7O3tRdm8Ys2aNVi1ahX09fVRVFTUrMtziOaNMsaqLnhjdfjwYbzxxhtkplRM+/bt8csvv2g6jEbD1dVV0yEwwZSxsrW1xe3bt7Fu3Tp4eXkhLS0NaWlp8PLywvr16xEeHg4bGxtVx0oQBEE0AU6fPi2YKnt7e7Rq1apB+3NwcBCdsXr27Bm+/vpr2Nvbo6ysDMXFxZoOiSCYKCoqQlFRkcqMVVVVFRYuXKiK0AhCdEg4juM0HURTIz8/H+bm5sjLy9P4XDGpVCratQo0CenGDmnHTkvR7tVXX8W1a9dQWlqKjh07Nnhx3xUrVuDMmTN48OCBiiJUPy+99BLOnz+PdevWYfbs2UhOToajo2OjxtBSzjd1QNr9R3x8PFxdXXHmzBkMGzas3u3r0i46OhqdOnWCt7c37t69K8rFa9UNnXfKIzbNxBNpC0VstaVNBdKNHdKOnZaiXUhICPz9/bFt2zaVlH07ODiIZhHIP//8EwsWLMCePXvw3XffwcnJCUD1U//GpqWcb+qAtPuPnJwcAIClpaVC29elHb/m0IIFC8hU1QGdd8ojNs0UmmM1ePBgpXcskUhw7tw5pd9HyHLt2jV06dJF02GIDtKNHdKOnZagXWZmJh4+fIhPPvkE/fr1U8k+7e3tkZeXh7KysiY9L0MqleK1114DUD2vbN68ebh9+zYAoLCwsNHjaQnnm7og7f6DL2NVdDHWurRzdnbGzp07MXnyZJXG15yg8055xKaZQsZKKpXWevrw9OlTxMbGwtzcHO3atQMAxMXFITc3F25ubnBxcVF9tARBEIRG4VvfqspUAf8tEpyent6k/3Zcv34dALB27VrMnDkTWlpawodRTWSsCEIV8MbKyMioQfuRSCSYPXu2KkIiCNGikLG6ePGizM8hISEYP348/ve//2H+/PnCIpCVlZXYunUrPvjgA2zbtk3VsRIEQRAaJjQ0FM7OzmjTpo3K9mlvbw8ASEtLg4uLCx4+fIh9+/Zh9erVKjsGC7GxsUhLS0OrVq3g4OCAjRs3ws7ODsuXLxc6AJqYmADQTMaKIFSBqowVQRCMzSt69+6Nfv36Ye3atXJff/fddxESEiI83RMbTal5RU5OjsJ1z8R/kG7skHbstATt+vXrh1atWmHfvn0q22dycjKcnZ1x7NgxjBkzBgMHDsTly5dRUFAgGBdN0LlzZ6G+XyKRgOM4bNu2DfPnzxe2yc7OhrW1NQ4ePIgpU6Y0anwt4XxTF6Tdf+zZswcvvfQSCgsLFSoHJO3YIe2UR2yaMTWviIiIEMr/5OHq6orIyEjmoIj/oPISNkg3dkg7dpq7dqWlpbh16xb8/f1Vul9bW1sA1Rmro0eP4vLlywCApKQklR5HGTiOQ3x8PN577z2cPHkSf/75Jw4ePChjqoD/Mlaa+L9v7uebOiHt/oPPWPHt0uuDtGOHtFMesWnGZKycnJywb98+VFZW1nqtsrIS+/btEzolEQ3j9OnTmg5BlJBu7JB27DR37W7duoXy8nKVzq8CAF1dXZiYmODp06d4//334eHhAaB6rShNkZ+fj5KSEvTo0QMjR47EK6+8IjcjpaenBx0dHY2UAjb3802dkHb/UVxcDAMDA4VbWpN27JB2yiM2zRSaY/U877//Pl5//XX07t0br7/+Otq3bw8AiImJwe+//467d+/it99+U2mgBEEQhGYJDQ2FiYkJvL29Vb5vR0dHrF+/HgUFBQgLC0Pv3r01aqxSUlIAQKGHhCYmJqJ7qkoQPMXFxQp3BCQI4sUwGavFixdDW1sbq1atwuLFi4WOgRzHwdbWFr///jteffVVlQZKEARBaAaO41BYWIiQkBD07t1baFikSiZPnozvv/8eCxcuRK9evWBjY6NRY8Wvq6XIor8mJibUvIIQLUVFRdS4giBUBPNfx0WLFmH+/Pm4desWEhISAABt2rRBjx491PJHt6UyZMgQTYcgSkg3dkg7dpqjdkVFRRgxYgRCQ0MBQG2d+l5//XWMHz9eyIa1atUK8fHxqKys1MjfFD5jpYixMjY21kjGqjmeb40FafcfxcXFShkr0o4d0k55xKYZ0xwrHh0dHfTu3RszZszAjBkzGvwk89tvv4Wfnx9MTU1hZ2eHiRMnIjo6Wu62HMdh1KhRkEgkOHLkiMxriYmJGDNmDIyMjGBnZ4eVK1fKnQ8mBqytrTUdgigh3dgh7dhpjtqtXr0ad+/exU8//QR/f39MnTpVLcextrZG3759hWYQTk5O2Lx5M0aNGqWW49VHSkoKTE1NFSqR0lTGqjmeb40Fafcfyhor0o4d0k55xKZZg4xVRUUFIiMjERISgsuXL9f6UpZLly5h6dKluHbtGoKDg1FRUYHhw4fLfRL4008/1Vq0GACqqqowZswYlJeX4+rVq9i+fTu2bduGzz77jOl31DT79+/XdAiihHRjh7RjpzlqFxERgVGjRmH58uW4cuUKPD091XKc57XLy8sDAJw9e1Ytx6uPlJQUhbJVQHXGqrCwEOHh4UIFR2PQHM+3xoK0+w9ljRVpxw5ppzxi04wpvSSVSvHRRx/ht99+E9p0yqOqqkqp/Z46dUrm523btsHOzg7h4eEICAgQxu/evYu1a9fi1q1btf7wnTlzBg8ePMDZs2dhb2+Prl274quvvsIHH3yAzz//HHp6ekrFRBAE0ZJJTk5Gp06dGv24P/74I8aNGyf3AVpjoIyx4ptXvPLKK+jYsSP27t2r5ugIQnUoa6wIgqgbpozVN998gx9//BFz5szBjh07wHEcvvvuO/z+++/w9vaGj4+PStoj8k8srayshLHi4mK89NJL2LhxIxwcHGq9JywsDF5eXrC3txfGRowYgfz8fPz7778NjokgCKIloYzBUCV9+vTBjz/+iMzMTJSVlTX68dPT02X+jrwIPmOVkZGBy5cvg+M4NUdHEKqDjBVBqA4mY7Vt2zZMnz4dmzZtwsiRIwEA3bt3x6uvvorr169DIpHg/PnzDQpMKpVixYoV6Nevn0zpydtvv42+fftiwoQJct+Xmppa648h/3Nqaqrc95SVlSE/P1/mq6nQo0cPTYcgSkg3dkg7dpqbdmVlZcjOzm6UdQnlaccfl28k0Zjk5OTIPNR7EXzGKicnBykpKYiNjVVzdNU0t/OtMSHt/kNZY0XasUPaKY/YNGMqBXz27Bnef/99AIC+vj4AoLS0FED1Yolz5szBunXr8M033zAHtnTpUty/fx8hISHC2NGjR3H+/HncuXOHeb/y+Pbbb/HFF1/UGt+xY4ewEvmsWbOQkpKCixcvCq+PHj0aurq6CAwMFMb69esHNzc37NixQxjz9PREr169sHfvXmG+WKtWrTBixAicPHlSaOtrZmaGadOm4erVq4iKihLe7+XlhaioKFy7dk0Ymzx5MoqKimQyg0OGDIG1tbVMPWqPHj3g4+ODrVu3QiqVAgA6dOiAgIAAHD58GNnZ2QAAOzs7jBs3DufOnUN8fDyA6v/bOXPmIDw8HHfv3hX2+dJLLyEpKQmXLl0SxsaMGQNtbW0cPXpUGPP394erqyv+/vtvmd+lZ8+e2LNnj1BG2rp1awwbNgwnTpwQzK+5uTmmTp2KkJAQmQYmixYtQmRkJG7cuCGMTZ06Ffn5+Thz5owwNnToUOTn5+PAgQPCmJ+fH7y9vfHXX38JT5Td3d3Rv39//PPPP8jNzQVQbcTHjh2Ls2fPCvMlDAwMMHv2bNy8eRMRERHCPufMmYPExESZOYVjx44FABw/flwYCwgIQOvWrbFz505hzNvbG35+fti1a5dw/bRp0wZDhw7F8ePHkZaWBgCwsLDAlClTcOXKFTx69AgAIJFI8PLLLyMiIgI3b94U9jlt2jTk5OTIzEsZPnw4zMzMcPDgQWGsZ8+e8PLywpYtW4Sxjh07wt/fHzExMbh16xYAwMHBAWPGjEFwcDASExMBAEZGRpg1axZu3LiByMhI4f1z585FXFyczDU7fvx4VFVV4cSJE8LYgAED4OzsjN27dwtjXbt2Rffu3bFz504hO9G2bVsMGTIEx44dQ3p6OoDq7PWkSZNw+fJlxMTEAAC0tLSwcOFC3Lt3T4gbAKZPn46srCycO3dOGBsxYgSMjY1x6NAhYax3797w8PDA1q1bhTEPDw/07dsXBw4cEB60ODk5YdSoUTh9+rTQBtzY2BgzZ87E9evXcf/+fQDVi+jOmzcPT548ETrpAcCECRNQUVGBoKAgYWzgwIFwdHTEnj17hLFu3brB19cXO3bsQEVFBQCgXbt2GDRoEAIDA5GZmQmgekLvxIkTcfHiRTx58gRAdUOh+fPn486dO7h9+7awz5kzZyI9PV3mgdfIkSNhaGiIw4cPC2N9+vRBx44dsW3bNgAQjuXo6Ih9+/YJDRqcnZ0xcuRInDp1CklJSQCqzcWMGTMQFhaGBw8eCPtcsGABoqOjERYWJoxNmjQJJSUlMuXfgwcPRlFRkUwZnZmZGQBg8+bNcHV1BQC4ublh4MCBOHLkCLKysgAANjY2mDBhAi5cuCCYGl1dXcybNw+3b9+W+Zuh6L08LS0NZmZmMtdIXfdyY2NjPH36VLinrVu3Dhs3bqx1L1+4cKHK7+UAmv293NLSUuX38vLycpn/2+Z0LzcxMcG4ceMQFBQkVP686F6enp6OyspKYR+K3Mtv3brV7O/lANRyLwfQ6PdyAOjcuTP69OnTKPdyOzs7mXu5r68vunXrhu3btwvN5JS5l/v4+DDfy1X5uXzRokWoF44BJycnbu3atcLP5ubm3IYNG4Sf161bxxkbG7PsmuM4jlu6dCnXqlUrLjY2VmZ8+fLlnEQi4bS1tYUvAJyWlhY3YMAAjuM47tNPP+V8fHxk3hcbG8sB4G7fvi33eKWlpVxeXp7w9fTpUw4Al5eXx/w7qIq//vpL0yGIEtKNHdKOneam3dWrVzkAXEREhNqPJU+7rKwsDgB34MABtR//eczNzbkffvhBoW0/+ugjztDQkAPAAeBefvllNUdXTXM73xqT5qpdUlKScB4+fPhQofd4eXlxb731lsLHaK7aNQaknfKITTOmUsBu3brJPFkZNGgQfvrpJ4SGhuLKlSv45Zdf4OPjo/R+OY7DsmXLcPjwYZw/f154Qsnz4YcfIiIiAnfv3hW+AGD9+vXCE4o+ffogMjJSeCoCAMHBwTAzM0Pnzp3lHldfXx9mZmYyX00F/skkoRykGzukHTvNTTu+BK8xSgHlaWdpaQkDAwPhSWpjUVVVhby8PIVLAR0cHFBSUgKgOntx5coVdYYn0NzOt8akuWrHZ5l0dXXx5ZdfKvQeZRcIbq7aNQaknfKITTMmY7V48WKUlZUJad6vv/4aubm5CAgIwIABA5Cfn4+1a9cqvd+lS5di586d2L17N0xNTZGamorU1FThD5aDgwM8PT1lvoDq8gPehA0fPhydO3fG3Llzce/ePZw+fRqffPIJli5dKpQtEgRBEPWTnJwMPT09hQ2GqpFIJHBychLKMhoLvpTM0tJSoe1rNvcYP348YmJi6pzTSxDqJDQ0FO3atcMvv/yCPXv24OHDh3Vuy3EcAgICEBsbS80rCEJFMBmr8ePH49ChQ4JR6dy5M548eYJDhw7h6NGjiImJQe/evZXe76ZNm5CXlyfUqvJf+/btU3gf2traOH78OLS1tdGnTx/MmTMH8+bNU/jJTVODr6EnlIN0Y4e0Y6e5aRcREYE2bdo0SsvzurRzcnJqcMbq8uXLMnN06iMnJwcAm7EaN24cAMjMTzl79izu3bun8PEVpbmdb41Jc9UuNDQU/fr1w8KFC9GqVSt89dVXdW577do1IbuqjLFqrto1BqSd8ohNMwnHKd8X9vLly/Dw8ICtra3c1zMzM/HgwQOZtafERH5+PszNzZGXl9ekygIJgiAai4KCAjg5OeGdd96R29ynsZA3WVtZAgICkJSUJEwMr48bN26gV69euHv3rkJl7bGxsXBzcwNQXVbl6emJcePG4eeffwZQXT7v6ekp0/yBINSBqakpPv/8c7z77rv4/fffsWTJEjx48EDuWnTLli3Dxo0bAQBr1qzBu+++29jhEkSzgyljNWjQIAQHB9f5+rlz5zBo0CDmoIj/qNnlhVAc0o0d0o6d5qQd3+3tlVdeaZTj1aVdQzNW+fn5CAsLQ2xsLAoKChR6D2vGSk9PD4aGhujfv7/MPKv09HShA5gqaU7nW2PTHLXjOA7FxcUwNjYGACFr9f3338vd/syZM8IDcGVKV5ujdo0Faac8YtOMyVjVl+QqKyuDtrY2U0CELHwLXUI5SDd2SDt2mpN2f/zxB0aPHg0XF5dGOV5d2jk7OzdojtXFixeF9r412yi/CN5YKTq3zNDQEObm5rC0tIREIkH//v1x79495Ofng+M4ZGRkqMVYNafzrbFpjtpVVlZCKpUKy8To6+tjzJgxcstQc3JyEBMTg1deeQW//vqrsISOIjRH7RoL0k55xKaZwutYJSYmCmtiAMDDhw9l1nvgyc3NxR9//IE2bdqoJECCIAiicQkPD8ft27c1WgLI4+TkhMLCQuTn5wul2YmJiSgvL0f79u3rfX9kZCQsLCxQUFCAiIgI9OnTp973ZGdnQ0dHR3jyr2ic/EPHnj17QiqVIjIyEp6enqioqFCLsSKImvCNvgwMDIQxe3t7mS7JPPw6UX5+fnLLBAmCYENhY7V161Z88cUXkEgkkEgk+Prrr/H111/X2o7jOGhra+OPP/5QaaAtFTs7O02HIEpIN3ZIO3aai3Z//PEHWrVqhVGjRjXaMevSztnZGUB1h0LeWPEP7hSZIlxcXAwLCws4Ozsr3EAiJydHyD4piqOjo7A4LG/4YmJi4ODgAABqMVbN5XzTBM1RO95Y8RkroPr3TE9PB8dxMufzzZs3YWZmBnd3d6WP0xy1ayxIO+URm2YKG6vp06fD09MTHMdh+vTpeOutt9C/f3+ZbSQSCYyNjdG1a1fY29urPNiWCN9hilAO0o0d0o6d5qBdUVERdu/ejZUrVzZqSXdd2vFraCUlJTE9WS8pKYGhoSG8vb0RERGh0HtycnKUbjE/fvx4FBYWAqjusObs7IzHjx8LMRcWFqK0tFQmm9BQmsP5pimao3byjJWtrS0qKiqQl5cHCwsLYfzs2bPo06cPtLSUnxHSHLVrLEg75RGbZgobKw8PD3h4eACozl4FBATUWsCXUD3nzp3DkCFDNB2G6CDd2CHt2GkO2oWEhKCoqAjTp09v1OPWpR1vrFjnWRUXFwvG6vjx47We3MsjOztb4cYVPMuXL5f5uUOHDoiJiUFGRoYwlpWVJWTgVEFzON80RXPUrq6MFVDdQIU3VikpKbh48SI2b97MdJzmqF1jQdopj9g0Y2peMX/+fLmmKjY2FlFRUQ0OiviPmvPaCMUh3dgh7dhpDtpdvHgR9vb2jT7voi7tjIyM0Lp1a1y9epVpvyUlJTAyMoKPjw8KCgqQkJBQ73v4UsCGIM9YqbocsDmcb5qiOWpXn7HiOXDgAHR0dDBp0iSm4zRH7RoL0k55xKYZk7HasGEDZs6cKTO2cOFCdOjQAZ6enujRo4fcyZIEQRBE3Rw5cgRbt27VaAwXLlzAwIEDG2VRYEWZNWsW9u7di7KyMqXfW7MUEIBC5YDZ2dlKlwI+D2+sHj58KIxRAwtCnfBz/GqWm8ozVnv37sXIkSMb/PCAIIjaMBmr//3vfzJzqE6fPo3t27dj8eLF2LBhA2JjY5tEN6nmgL6+vqZDECWkGzukHTsN0e7p06eYM2cOXn/99Qat29QQCgoKcOvWLY2sQ/gi7ebPn4/c3FwcO3YMUqlUqf3yxsrJyQmWlpaIjIys9z2qyFiNHj0aurq6+PHHH6GjU111r2pjRdcqO81RO3kZK0tLS2hrawvGKj4+HmFhYbUejitDc9SusSDtlEdsmjEZq4SEBGG+FQDs378frq6u2LRpE5YsWYJly5YhKChIZUG2ZObMmaPpEEQJ6cYOacdOQ7Rbvnw5zMzMYGRkhI0bN6owKsUJCQlBVVUVBg4c2OjHfpF2Hh4e8PPzw/bt25GXl6fUfnljJZFI4Orq2milgF26dMHdu3cBVK8vpKurq3JjRdcqO81RO3nGSktLC7a2toKx2r9/PwwNDTF+/Hjm4zRH7RoL0k55xKaZShYIPnPmjExb3rZt2yq1ijdRN+Hh4ZoOQZSQbuyQduywanfixAkcPnwY69evR/fu3fHkyRMVR1Y/sbGx+Prrr+Hg4MDUgrmh1Kfd/PnzcfLkSURHRyu1X755BQC0bt0aT58+rfc9qigF5I9369YthISEwMbGRuXGiq5VdpqjdvKMFfBfy3Wgugxw7NixMDExYT5Oc9SusSDtlEdsmjEZK3d3dxw+fBhAdRlgcnKyjLF69uyZTFtPgh3+iSehHKQbO6QdOyzalZSUYNmyZRg2bBimT58Oc3NzpbMyqmDJkiUIDQ3V2Pyq+rSbOXMmtLS0ZLJ5iqxjxTevAAAXF5d6jVV5eTmKi4tVNv+ke/fu6Nevn1qMFV2r7DRH7eQtEAwAFhYWyMvLQ1xcHO7cuYMZM2Y06DjNUbvGgrRTHrFppnC79Zq89957eOmll2BpaYmioiJ4eHhgxIgRwuvnz59H165dVRUjQRBNmJSUFDg4ODSpZgdi4vr164iPj8c///wDiUQCc3Nz5tbiDSEuLg5+fn5Yv359ox9bEaytrTFu3Djs3LlTGKuoqICent4L38eXAgKKGaucnBwAUPnEfnUYK4KoSWlpKSQSSa05KUZGRiguLha6q/n4+GggOoJoGTBlrGbOnInTp09jwYIFWLVqFS5cuCBMzuVLKBYvXqzSQAmCaHqcOHECTk5OOHXqlKZDES3Pnj0DAKG9uSYyVlVVVYiPj8fcuXPh4ODQqMdWhpdeeknmZ74L2ot43ljl5+e/UN/s7GwAUEkpYE3IWBF1wXEcpk2bhosXLzZoPyUlJTAwMKj1kIs3VllZWQCqH1IQBKEemDJWADBs2DAMGzas1riVlRUOHTrUoKCI/3j+gwShGKQbO4pqx3EcFi1aBAC0vML/R5nzLjs7G/r6+khKSoKFhYVQrqYJY5WUlITy8nK0b9++UY9bE0W0e36RyNLSUpiZmb3wPTXnWLm4uACo7sBobm4ud3t1ZqxiYmJUuk+6z7HTlLTLz8/HwYMHcfDgQVRWVkJbW5tpPzUfItTEyMgImZmZyMrKgpaWVp3nvqI0Je3EBmmnPGLTjCljRTQemmq7LHZIN3YU1S46OhppaWkAgKKiInWGJBqUOe/Gjx+Pjz/+GM+ePYOzs7Mwzs+HqIlUKsUPP/ygtm6rfLMMNzc3texfERTR7vm5uywZKwAy5YDFxcUy62PxGSsxlALSfY6dpqRdzUWkg4ODFXpPVVUVPvnkEyHjDbzYWPEZKysrK2hpNeyjX1PSTmyQdsojNs2Yri5XV1e0a9fuhV+a/APdnLh06ZKmQxAlpBs7imoXEhICLS0t6OjooKCgQM1RiQNlzruoqCjcu3cPSUlJaNWqlTBubm6OoqIiVFRUCGMff/wxPvjgA7WtD/j48WNoaWmhbdu2atm/Iiiq3RtvvCF8X5+x4jhOpnmFk5MTtLS0ZIyVsbExRo4cKfys7jlWijTcUBS6z7HTlLSraazOnz+v0HuioqLw9ddfw8vLC1VVVQD+KwV8HmNjYxQVFSEzM1MlZYBNSTuxQdopj9g0YyoFHDBgQK0a3qqqKiQkJCA0NBSenp7o1q2bSgIkCKJpcuXKFXTt2hWZmZkt3lht3LgRurq6CpfwFBYWIjs7GzExMWjVqhU8PT2F1/gynfz8fFhbWyMrKwsbNmwAAOjq6qo+eAD//vsv2rRpU28jiKbAxo0bsWDBAvTq1ateY1VRUQGpVCo8xdfR0YGjoyOePn2KI0eOYNKkSQAgM7clJycHBgYGcp/8NwQbGxuUlpaiuLgYxsbGKt03IW54YzVkyBBcuHBBoffwZaW5ubnYv38/Zs2ahdLS0nozVjS/iiDUC5Ox2rZtW52v3bt3DyNGjMDs2bNZYyIIogkSGxuLESNG4Pr167CyskJISAjGjh2Lc+fOtXhj9ccff8DZ2RlTp05VaPvExEQAQHJyMoqKimS6qvLGKi8vD9bW1ti0aROkUinmz5+PsLAwlcfOcRxOnDghd85sU0QikQgfHuszVvLW9eE7AxYWFgpjPXv2FL7Pzc1Vy3IhNjY2AIDMzEwyVoQMvLGaOnUqli5diqtXr6Jv374vfM+jR49gZmYGf39/fPnll5g+fbpCpYBkrAhCvah8jpWPjw9ee+01fPDBB6redYtkzJgxmg5BlJBu7NSl3b///ovHjx8jISEBycnJiI2Nhb+/P0xNTVu0saqoqMDDhw9RWFio8HmXkJAgfJ+Xlyczx6qmsSotLcWGDRuwYMECdO7cWS1NQqKjo/H48WOMGzdO5ftWBmWuWb7cqT5jVVxcDEC+sZJKpbC2tsaIESMEAwZU697Qyf3yqGmsVAXd59hpStplZGTA0tISL730Evr27YsBAwbgl19+eWHZaExMDDp06IDVq1fj4cOH2L9/v0LGij8PG0JT0k5skHbKIzbN1NK8wt7eHg8ePFDHrlscrN2BWjqkGzt1acdP6s/Pz0dISAgAkLFCtTGpqKhAUVGRwuddYmKiTDm1l5eX8H1NY7Vjxw5kZGTgnXfegZ2dHXJzc1FeXq7S+I8ePQpDQ8NaHfcaG2WuWUWN1YsyVrm5uejUqRN69OiB/Px84fXGyFipCrrPsdOUtMvIyICtrS3MzMxw/vx5LF++HMuXL8crr7wCqVQq9z28serZsydGjx6Nr776CkVFRY2SsWpK2okN0k55xKaZyo1VVlYWtmzZIjMZm2Dn6NGjmg5BlJBu7NSl3fPGys3NDY6Oji3eWN2/fx9AdWdERc+7xMREuLi4oG3btnjttddkyn74D/U5OTlYu3YtJk2ahA4dOsDOzg6A7ER3VXDs2DEMGzZM5XOKlEWZa1ZZY8U3rwD+M1Y5OTmwtLSEmZmZaI0V3efYaUra8cYKqJ5HuWbNGuzYsQNbt27Fpk2b5L7n0aNHcHd3BwCsXr0aUVFROHPmTJ3NKziOQ1JSkkqMVVPSTmyQdsojNs2Y5lgNHjxY7nhubi4ePnyI8vJy/P333w0KjCCIpgVvrPLy8hASEgJ/f38AgKmpKVJTUzUZmkaJjIwEAJk5O/URFxeH1q1b49KlS7VaH/MZq4MHD+LRo0fYunUrAAgfvDIyMmRKBxtCZmYmrl69ij///FMl+2ssGpqxKi0txZMnT+Dr6wtTU1Pk5+eD4zhIJBJhbpuqMTIyEtYTIoia1DRWPHPnzsXPP/+MiIiIWtsnJCQgNTUVXbt2BVA9R3DUqFE4efJknRkroLo0luZYEYR6YcpYSaVScBwn8wVUt2FftmwZ7t+/j1mzZqk0UIIgNAtvrJ49e4Z79+6hf//+ANDiM1a8sVJmLa+wsDD06NFD7noyenp6MDAwwO7du9GxY0f06dMHAISMlSrnWQUFBUEqlYquhr0hc6xat24NoLqE08LCAmZmZqiqqhJMmLoyVoB61rIixI88YwVUt/zn2//X5MKFC5BIJBgwYIAwtnr1agB4obECoJI5VgRB1A1Txqpma1pCvfBZAUI5SDd26tKON1anTp2CVCqVyVi1ZGN1//59mJqaorCwEP369at3+8TERMTHxyMgIKDObfz8/HDlyhXMmTNHmIvFf/BSpbE6evQoevXqBQcHB5XtkxVlrlkdHR1oaWkxZ6yA6iVCeGMFAAUFBTAyMlJb8wpA9caK7nPsNCXt0tLSYG9vX2v8Rcaqa9eusLKyEsZ69eqFZcuWwc/Pr9b2NY2VKq71pqSd2CDtlEdsmqmleQWhOlxdXTUdgigh3dipSzveWF26dAnW1tZCfX9LNlYFBQWIi4tDz549UVVVpVCJ3pUrVwC8+I/F6dOn8ddff2H58uXCmJGREUxMTFQ2x6qsrAynT5/WeDdAHmWuWYlEAgMDA7z22msIDAysczt5xsrOzk5YD6ymseLnWYkpY0X3OXY0qV1SUhIWL16MkpISlJeXIzk5Wcik1qQuY3Xt2jW5948NGzZg3rx5tcZVbazovGOHtFMesWmmkLHasWMHduzYIZT88T/X97V7926cOXNGZmIwoRw0V40N0o2durTjjRUAtG/fXsikNEVjlZeXh7feekupeU8s/PvvvwCA3r17AwD++uuvet9z+fJldO7cWW7pD4+hoSEWLlwIU1NTmXEbGxuVGavw8HAUFhbKrKGlSZS9Zvkyv9OnT9e5TWZmJrS0tGQyUFpaWkJzpeeNFcdxospY0X2OHU1qd/36dfzvf//D1q1b8ezZM0ilUrRt27bWdvKMVWVlJWJjY9GpUyeFj1dz3TR5mTFlofOOHdJOecSmmUKlgAsWLIBEIsHMmTOhp6eHBQsWKHUQY2NjHDx4sMn8AScIQnlqGisnJyfhe1NTU5SXl6O8vBx6enqaCK0WwcHB2LBhA6ysrPD555+r7Tj379+HlpaWUH5TVlYmdztvb2/MmzcP7733Hi5fvoyBAwcyHc/a2lrm/4GV4uJihIaGwsjICD4+Pg3enyZ50dIecXFxaNWqVa3z0sXFBXFxcUJXQKDaWJWUlKCiokKtGSt5zQiIlgWfSf3xxx/RoUMHAECbNm1qbSfPWCUmJqKyshLt27dX+Hg1M1Y1vycIQvUoZKzi4uIAQPjjxP9cH1VVVUhOTsZHH32E9957j4wVQYiYrKws4fvnjRVQXRbXVDpO8Y0kAgMDG2ysqqqq6lxHIzIyEu3btxcmhMszVmVlZYiMjMTKlSsxatQoPHz4EJ999hlTLFZWVjL/DyxUVVXBz88PDx48wIABA4SyOLHCZw3lERcXJzcTwM+zej5jlZubCwCiyVgR4oSfGxgfH4/vv/8eAOosBczNzYVUKhUa3Tx58gQAmI0VQRDqRSFj9fyTFHlPVuqiXbt2WLhwIV577TXlIiMAyC4cSigO6caOPO0qKyuRl5cn/FxzLlHND6ZNxVjx7d/v3r1bZ8ctRUhKSkKrVq1w/PhxuZ3zIiMj4eXlJZTa8B/Ya1LTCH3wwQcAIHRUVBZra+sGN684efKkkOVR5sOZumG9ZjMzM+v8P46Li0PHjh1rjdc0VvyDgfz8fOEcV/ccK761e0Oh+xw7mtSutLQU+vr6GDJkCIKCguDg4CB3/SlLS0twHId79+5h/vz5eO+991BYWAgdHR25RqwuVG2s6Lxjh7RTHrFp1ijNK15++WVUVFQ0xqGaHT179tR0CKKEdGNHnnZ8+ZmlpSUA2YzV85P/mwJpaWnQ0al+bnTnzh3m/SQnJwMAlixZIvf1+/fvw9PTUzBW8rIjNTMUJ06cQLt27ZgXUFc2Y8VxHAYMGIBLly4BqF7/5t1334Wfnx/Wr1+Pjz/+mCkOddCQa7aucsC4uDi5E59rGit9fX3o6urKZKzUaawqKytVdq3QfY4dTWpXUlICAwMDfPTRRwDqfljN329Pnz6NyMhIzJ8/H6tWrYKrq6twf1MEeaatIdB5xw5ppzxi04zZWKWmpuLrr7/GlClTMHToUAwePFjma8iQIaqMs8WyZ88eTYcgSkg3duRpFxwcDADC0/+axor/EMp/KNU0q1evRnBwMPr27QszMzPcvn2beV98yU5iYqKwXhVPWloaMjIy4OXlBRMTEwDV60I9D2+E+AYXL2qzXh/KzrHKycnB5cuXERYWBgD49NNPUVhYiF27dmHFihVo164dcyyqRtlrNjY2FsnJydDR0ZFrrEpKSpCWlibXWPXo0QOOjo6wt7eHRCKBmZkZ9uzZI1RW1GxjrUr4klFVlQPSfY4dTWpXWloKAwMD+Pv7Y+jQofD29pa7HW+s7t+/DxMTEwQGBsLQ0BC+vr5KHU/eenkNgc47dkg75RGbZkzrWEVERGDgwIEoKSlBx44dERkZic6dOyM3NxdJSUlwc3OTWxJDKA/f+YpQDtKNHXna7d69G/369RNMVFM1Vvfv38eXX34JAJgxYwYkEkmDjBU/yVxHRweffvopjhw5Iry2ZcsWANWNKfiMVc1ySR7+Q/SoUaNw7dq1BhmrF2WsKioqas2XSklJAVD9IKyyshInTpzA66+/LkyYb0ooe83yhsnd3V3uPKv4+HgA8rOIPXv2FLKR/Db379/HqFGj8Nlnn8mc36qE/6CcnZ0NNze3Bu+P7nPsaFI73lgB1Q9j6jI+NY2Vs7Mzxo8fjxEjRkAqlTIdd/r06WwBPwedd+yQdsojNs2YjNWHH34IExMT3L17F0ZGRrCzs8PPP/+MwYMH48CBA3jjjTewa9cuVcdKEIQGuHPnDk6dOoXffvsN+/btAwA4OjoKr/PGSt56K43N9u3bhe/t7e3h6OiIY8eOMe+Pv6H/+OOPePvtt3Ht2jXs2bMHdnZ2+OSTT/Duu++iQ4cOqKqqAgCUl5fX2kdmZia0tbUxceJErFmzpkHZfGtraxQXF8t8MAOq58AZGxujf//+OH36tFAmVNNYhYWFITs7u8msW6UqOnfuLDdjxTdZUmQNlNDQUGhpaam9kQef2eSbqxAtk5KSEmFttRedczWN1YABAwAA+vr6TMdMS0tTW4krQRD/wZQfDg0NxWuvvYbWrVsLT1r4JyjTpk3D7NmzsXLlStVF2YJRZoIq8R+kGzs1tauqqsJrr72Gzp074+WXX8Zvv/2GpUuXCn/wgepuoUZGRhrLWFVWVuLnn39Gt27dsGbNGmHczs4Ovr6+ePLkidxMkiLwGatFixbB09MTr7/+On755Rd8+umnMDAwwP/93/8BALS1tWFgYACJRAKO45CWlibsIzMzEzY2NvD29kZ+fn6Dzk2+RO35csDc3FxUVFTg/PnzMlm1msbq2LFjsLOza7L16qy6vMhY6erqKpR94udZqRs+s6mq9dXoPseOJrV7/sFIXZibm0NLS0vhxcdfhJ2dncqWw6Dzjh3STnnEphmTsZJKpcIicxYWFtDW1pb5Q+/l5YXw8HDVRNjCGTZsmKZDECWkGzs1tfvzzz9x8+ZN/P7779DV1UWnTp3w66+/1upoJm+9FXUTGhqKJ0+eYPv27Xj77bfh6uqKwMBAHDp0CEB1tomfi3D37l2mY/AZK2NjY/zf//0f7t27B6C6KYS/v7/Mh6PS0lJs3boVU6ZMgbOzMxITEwFUz7FSVbfEFxkrnv379wvfP2+sxowZo/L5FqqC9Zrt3Lkz0tLSapVIxsXFoU2bNnW2ytcEqs5Y0X2OHU1qp6ix0tLSEtaZa6ixUiV03rFD2imP2DRj+gvr6uoqlFloaWnB1dUVZ8+eFV6/evUqpZxVxIkTJzQdgigh3djhtUtLS8NHH32ERYsWoV+/fi98j4WFRaNkrCorKwEA0dHR8Pf3R/v27bF79264ubnh0KFDGD9+PPr06QOguklEx44dYWhoyDzPqqSkBPr6+tDS0sL48ePh7+8vlOQMHTpU7nsOHz6Mqqoq4eESn7FSBbxBe95E8NpPnz4dJ06cEAwhb6weP36Mhw8fNukyQNZrtkuXLgCAqKgomfG6OgJqEr7ttaoyVnSfY0eT2pWWlgqlgPXB32fUNe+PBTrv2CHtlEdsmjEZq+HDh+PAgQPCz2+88QY2b96MoUOHYsiQIdi+fTteeukllQXZkuHX4yGUg3Rjh9ful19+gUQiERawfBGNkbHas2cP9PT00K5dO4wdO1Z4eHP+/HmZD9AODg6QSqUYMWIEdHR04O3tzWysiouLhQ/DEokEZ8+exZkzZxAcHIylS5fKbLtkyRKh9TwAoYugKo0Vn7Gqy1i9+uqrKC4uFroT8saqqqoKenp6TfrJH+s126FDB2hra9dqYBEfHy+3cYUm0dbWhqGhocqMFd3n2NGkdny7dUXo1asXgOoseVOBzjt2SDvlEZtmTMZq1apV2LNnj7A21YoVK/Dll18iKysLeXl5+PTTT4W5BwRBiJPo6Gj06NFDoTK2xshYnTp1Cu3atcOkSZPQvn17/PHHH8LCgc+3Da9Zqujr68u8llXNSeZA9VwcPT09DB06VCjr4tm4cSPeeustANUT0iMiIgCo1lhZWlpCW1sbGRkZMuO8qe3Rowe6du0qPPhKSUmBnZ0dAGDw4MG1Ym4O6Ovro3379rXmWTXFjBVQXQ5IzStaNoqWAgLA+PHj8cUXX2DBggXqDYogCJXAZKwsLS3RvXt3YbKvRCLBJ598gjt37uDWrVv4/PPPVTZJsqVjbm6u6RBECenGDq+dMh9MGyNjdfXqVYwZMwZr167FyZMnMX36dHh4eAB4cec3X19fREVFMbVsLS4uVrhkB6huvX7y5EksXrxYJmOlqjlW2tracHBwkGkVDlRnrPj1mKZNm4bjx4+jqKgIT548QY8ePQCgSZcBAg27Zp9vYJGXl4ecnJwmaayMjY1VlrGi+xw7mtROGWOlq6uLzz77TCYbrmnovGOHtFMesWnWNGcxEwJTp07VdAiihHRjh9dOmVIqeRmr0NBQlJWVqSSmtLQ0PH78GH379pUZ79y5M4DaGaua+Pr6QiqVChkkZSgpKRFKARVh2rRpGDlyJLp164aYmBgUFxcjKytLZRkroHquhTxjZWZmBi0tLUybNg3FxcX46quvkJSUhLfffhtff/01Zs+erbIY1EFDrtnnjZUyrdYbG1VmrOg+x44mtXs+Ey426Lxjh7RTHrFpRsaqiRMSEqLpEEQJ6cZOSEgI8vPzkZ2dzZyx+vfff+Hv749NmzapJCZ+jtTzrcIVyVh16dIFOjo6TPOslM1Y8eedt7c3OI7D7du3UVhY2CjGim+B36FDB3Tt2hXff/897O3tMWjQIHz88cdN/qlfQ67ZLl26IDk5WTD3vLFqanOsgGpjxZKxKikpqZUVPnfunNCpklAOTf6NUCZj1RShv6/skHbKIzbNyFg1caKjozUdgigh3diJjo5GfHw8AMU/mFpYWCApKQmnTp1CeXk5zpw5AwAqa+2dlJQEiUSCVq1ayYyPHDkSq1atEloSy0NfXx+enp5M86yUzVjx512XLl0gkUhw4cIFAFC7scrJyZHpxPrhhx+iR48eWLVqVZNqN/4iGnLN8pnLQ4cO4fTp04iLixMWr29qKFsKGBUVBT8/P/j4+AjNS3gWL16Mrl27qjjCloEm/0aI3VjR31d2SDvlEZtmOpoOgCCIpoeyxor/ADtq1CjY2tqqvMwlOTkZdnZ2tRZxNTMzU6hRjq+vb6NkrHiMjIzQvn37RjNWubm5MsZqxowZmDFjhsqO2dRxd3eHlpYWFi1aJIx17ty51nprTQFlSwGvX7+OW7du1RovKipCbGysKkMjGgllugISBCEuKGNFEEQt4uLiYGBgAAcHB4W2nzJlCs6cOYM7d+5gzpw5qKqqAqC69XpSUlLg6OjI/H5fX19ERkaivLxcqfcpm7Gqibe3N65evQoAKmteAVQbq/T0dKEr665du7Bnzx6hFLAlYmhoWGueXevWrTUUzYtRthTweRPNc/ToUeH7ptSKm6gfZdaxIghCXJCxauLUfAJLKA7pxs6iRYsQHx+PNm3aKPzE38DAAMOGDUPXrl2xbt06PHv2DK6uriozVsnJyQ1aILNbt26oqKiotdZRfSg7ybzmeefl5SU071B1xgr4b22POXPmAKguMRMzDb1m+XJAfl4fP8+qqaFsKWBdxurkyZPC9/yDDEJxNPk3QuylgPT3lR3STnnEphmzsUpMTMTrr7+Ojh07wsrKCpcvXwZQ3Vr4rbfeYprP8O2338LPzw+mpqaws7PDxIkTZWors7Oz8eabb6Jjx44wNDRE69at8dZbbyEvL69WbGPGjBFq7FeuXInKykrWX1Wj8C2bCeUg3diJjIxUyeKqrJP05dFQY+Xj4wOJRFJnOeDOnTsxe/bsWsar5gLBilDzvPP29gYA6OjoqLRVMv//sn37dmRnZwvjLF0PmxINvWb5OUivvPIKevfujW+//VZFkakWZUsB+UWeeSorKyGVSnHq1CnY29sLY4RyaPJvhNhLAenvKzuknfKITTMmY/XgwQN069YN+/btg6urK/Ly8oQbu42NDUJCQvDrr78qvd9Lly5h6dKluHbtGoKDg1FRUYHhw4cLf4SSk5ORnJyMNWvW4P79+9i2bRtOnTol42arqqowZswYlJeX4+rVq9i+fTu2bduGzz77jOVX1Tg3btzQdAiihHRj58aNGypZXLUpGStjY2O0b98eN27cwMcff4ySkhLhtYyMDMydOxfHjh3DgAEDZF5TNmNV87zjFy+2sbFR6VyfTp064dNPP8Wnn36KhQsXAgDGjh2LNWvWqOwYmqCh1+zKlSsRFhYGHR0dhIWFYdKkSSqKTLU0tBSwoKAA9+/fR0ZGBjp27AiAjBULmvobIZVKUV5eLupSQPr7yg5ppzxi04ypecX7778PCwsLXLt2DRKJpFbnpTFjxmDfvn1K7/fUqVMyP2/btg12dnYIDw9HQEAAPD098c8//wivu7m54euvv8acOXNQWVkJHR0dnDlzBg8ePMDZs2dhb2+Prl274quvvsIHH3xACxcThILEx8dj1qxZDdqHqoxVVVUVUlNTG2SsgGpDsn37dpSVlWHAgAEYMWIEACAhIQEA8M033+DNN9/Eo0ePhC6DymasatKuXTsYGRmpdH4Vz5dffgltbW18/vnnsLCwQGBgoMo6MIoVU1NTmJqaajqMelG2FDAlJQUSiUSYR1VQUIBr165BW1sbbm5uuHz5MhkrEcGXB4s5Y0UQRN0w/SW+fPky3njjDdja2sp9Etu6dWskJSU1ODi+xO/5FrPPb2NmZgYdnWqPGBYWBi8vL6FEAgBGjBiB/Px8pedXEERLpKioCHl5eWorBXz27BksLS0V7mj29OlTSKXSBjWvAKrXvOI/1NQsCUxMTAQADBs2DADw6NEj4bWGLOSppaUFT09Plc6vqsnq1avx008/4f3332/xpkpMKFMKyHEckpOTMXfuXPj5+QGoNlbXr1+Hp6enYPppjpV44DPiZKwIonnClLGSSqUvfIqbkZEBfX195qD4Y6xYsQL9+vWDp6en3G0yMzPx1VdfYfHixcJYamqqjKkCIPzMT/Z+nrKyMuEDFwDk5+c3KHZVIrYVp5sKpBs7/Lo4qigFzMzMrDUeHR2N3NxcREdH1+rkJo8PP/wQ1tbW6Nu3b4Pi6dSpk/B9TWOVkJAAQ0NDuLu7w8rKCjExMcJrymasnj/v3nvvPbV+6F2+fLna9t3YtJRr1tjYGBUVFSgvL6+3giIrKwsVFRWYMGECVq5cCS8vL8FY9e3bF/3798fGjRspY8WAps630tJSAOI2Vi3lWlUHpJ3yiE0zJmPl6+uLEydOYMmSJbVeq6ysxN69e9G7d+8GBbZ06VLcv3+/zhWX8/PzMWbMGHTu3Bmff/55g4717bff4osvvqg1vmPHDuFp9axZs5CSkoKLFy8Kr48ePRq6uroIDAwUxvr16wc3Nzfs2LFDGPP09ESvXr2wd+9e4Ullq1atMGLECJw8eVKooTczM8O0adNw9epVREVFAQDKy8vx2muvISoqCteuXRP2OXnyZBQVFeH06dPC2JAhQ2BtbY39+/cLYz169ICPjw+2bt0KqVQKAOjQoQMCAgJw+PBhYfK7nZ0dxo0bh3PnzglrGOnr62POnDkIDw/H3bt3hX2+9NJLSEpKwqVLl4SxMWPGQFtbW6YFsL+/P1xdXfH3338LY15eXujZsyf27NmD4uJiANUZzmHDhuHEiROC+TU3N8fUqVMREhIi08Bk0aJFiIyMlKm5nTp1KvLz84VFaYHqxgEdO3bEgQMHhDE/Pz94e3vjr7/+Espq3N3d0b9/f/zzzz/Izc0FUG3Ex44di7NnzwplYgYGBpg9ezZu3rwp0yRgzpw5SExMFJq3ANXzXQDg+PHjwlhAQABat26NnTt3ysTo5+eHXbt2CX9s27Rpg6FDh+L48eNIS0sDUL347pQpU3DlyhUhmyKRSPDyyy8jIiICN2/eFPY5bdo05OTk4OzZs8LY8OHDYWZmhoMHDwpjPXv2hJeXF7Zs2SKMdezYEf7+/ti5cyckEgmuX7+OjIwMjBkzBsHBwUJmx8jICLNmzcKNGzdkJpXOnTsXcXFxwjX79OlT5ObmIjU1FSdOnBC24zPRBw8eFM79rl27onv37ti5c6fwkKNt27bw9/fHvn37MHPmTAQGBsLKygqTJk3C5cuXBQOkpaWFhQsX4t69ezLr/UyfPh1ZWVk4d+4cAODJkycAqptJnD9/Hm+88Qby8vIQFxeH1q1b46+//oKFhQVOnDiBgQMHom/fvigqKsKdO3ewZcsWODk5YdSoUTh9+jSePXsGoPpD8syZM3H9+nXcv39f+LA8b948PHnyRHhIs2XLFkyYMAEVFRUICgoSYhw4cCAcHR2xZ88eYaxbt27w9fXFjh07hJbq7dq1w6BBgxAYGCiYVWtra0ycOBEXL16U+d3mz5+PO3fuyJjHmTNnIj09HefPnxfGRo4cCUNDQxw+fFgY69OnDzp27Iht27YJY507d0afPn2wb98+IQPp7OyMkSNH4tSpU0J1gomJCWbMmIGwsDA8ePBAeP+CBQsQHR2NsLAwYWzSpEkoKSmRKf/29PSEp6cn9u7dK4z5+vqiW7du2L59u2Ae3NzcMHDgQBw5cgRZWVkAquexTZgwARcuXBAyobq6upg3bx5u374t00xJU/dyAFi4cKFwTmzcuBFmZmYvvJd/9913AIB79+4Jf4t27tyJBw8eoEePHsK+jx07JlSPNLd7+dChQ2Fpaanye/n169fx9OlTYZ+NdS/v1q0bAODChQtITU1V67384MGDwv3WwcGB+V4OAOPHj0dVVRVOnDgh3OcGDBgAZ2dn7N69W9iurnv5kCFDcOzYMaSnpwNAg+7lQHUlkrGxMQ4dOiSM9e7dGx4eHti6dasw5uHhgb59++LAgQPCtafIvZyHv5eHhoYKYw25l/P3quZ8Lx88eDDs7OxUdi+vqqrC4sWLm8S9XKEOhRwDQUFBnJaWFvf6669zFy9e5CQSCbd7924uODiYGzRoEKejo8NdunSJZdccx3Hc0qVLuVatWnGxsbFyX8/Pz+f69OnDDRkyhCspKZF57dNPP+V8fHxkxmJjYzkA3O3bt+Xur7S0lMvLyxO+nj59ygHg8vLymH8HVbF582ZNhyBKSDd2/P39OS8vrwbvZ+XKlVyHDh1qja9du5YDwK1Zs6befTx79owDwB0/frzB8eTl5XFmZmbckiVLOAAyX8OHD+c4juPmzp3L9enTh+M4jquoqOAAcH/99ZfCx6Dzjp2Wol1ISAgHgHvw4EG9286fP59r3749J5VKuaysLA4A9+abb3IAuMjISO7tt9/mAHDx8fGNEHnzQlPn2/379zkAXGhoqEaOrwpayrWqDkg75RGbZkyF+aNGjcK2bduwb98+DB48GED1057hw4fj9u3b2LFjBwICApTeL8dxWLZsGQ4fPozz58/LLUXKz8/H8OHDoaenh6NHj9ZKp/fp0weRkZHCUxEACA4OhpmZmbDOyfPo6+vDzMxM5osgWioxMTHw9/dv8H7qmmPFP8nOyMiodx/8Nra2tg2Ox8zMDFlZWdiwYQMeP36M7OxsockOP+/B3d1deHrKP/W2sLBo8LEJgoefcyevTLYmRUVFOHjwIObNmweJRCI05jh79ixMTEzg4eEBbW1tADTHSkzwT8fFvu4cQRDyYSoFBKpTxZMnT0ZwcDBiYmIglUrh5uaGESNGMHdmWrp0KXbv3o3AwECYmprKlBIYGhoKpqq4uBg7d+5Efn6+kNq1tbWFtrY2hg8fjs6dO2Pu3Ln44YcfkJqaik8++QRLly5t8LwvgmjuZGZmIi0tTWXGqqCgoNY4XxajiLHiP3yqwlgBEJrcuLm5AagubwGqS2aB6jLZzMxMZGdnC8dWV/MJomWiqLE6dOgQioqKMHfuXADVpY36+vqIiorCoEGDoK2tLTQtoTlW4oGMFUE0b5Q2VsXFxXBxccGHH36IlStXYuLEiSoLZtOmTQCqa1VrsnXrVixYsAC3b9/G9evXAQDt27eX2SYuLg5t27aFtrY2jh8/jjfeeAN9+vSBsbEx5s+fjy+//FJlcTYmQ4cO1XQIooR0Y4Ofc+Du7t7gffHdz6RSqUzXOv6ByYkTJ/D+++/jhx9+qHMfvPlSl7kxMDBAZmamkKXmf++YmBiZmnhFofOOnZainYWFBbS0tOo1Vjt27MCAAQNkunOampqirKwMvXr1AgDhXzJWyqOp843P4puYmGjk+KqgpVyr6oC0Ux6xaaa0sTIyMoKOjo5anrZw/38Sal0MHDiw3m2A6kmjNScVihlLS0tNhyBKSDc2+BLa59emY8HExAQcx6GkpETmfsEbq7S0NPz444/4/vvv61xAl+8wqs4PITXXmerQoQOAamPFH1MZY0XnHTstRTttbW1YWVm9MGP77NkznDt3TqYhAVBtrDIzMwVDxWtGxkp5NHW+NYeMVUu5VtUBaac8YtOMaY7VlClTcPDgQYVMDtEwanZCIhSHdGODN1aqKL3jjcnz86zS0tJkjBQ/l0kemZmZda6Xpw5MTEzg6OiIR48eITMzExKJRKmbOp137LQk7WxsbF6Ysdq5cycMDAwwZcoUmXG+zJ43VhcuXABAc6xY0NT5xt8PWRcebwq0pGtV1ZB2yiM2zZjmWM2cORNLlizBoEGD8Oqrr6Jt27ZyF9H09fVtcIAEQTQe6enpMDAwYF4UtyY1jRW/llxZWRkyMjLQunVrof1xenp6neYlIyNDZfOrFMXd3R2PHj2CsbExLC0thXlZBKEq6jNWZ86cwciRI2s1UjI1NYWLi4uwWDbNsRIfRUVFMDQ0FBqPEATRvGD6xFBzDtSVK1dqvc5xHCQSCT1FIwiRkZ6eztx85nn4/WRnZwvNIn777TcA1eus1DRWHTt2lLsPTRmr8PBwuLi4yJQJEoSqqM9YZWRkwMvLq9a4q6urzLVCxkp8FBUViXp+FUEQL4bJWNVcfI1QL35+fpoOQZSQbmykp6fDyclJJfvy9PSEoaEhDh06hKCgIBw9ehS3b9/G4sWLsXTpUty7dw9paWkySyM8T0ZGBlq1aqWSeBSlQ4cO2LNnD7y8vJRumkHnHTstSTsbGxvcu3evztezsrJgZWVVa3zbtm0yJfhdu3YFQMaKBU2db4WFhaKeXwW0rGtV1ZB2yiM2zZQ2VmVlZbC0tETbtm3h7e2tjpiIGpDGbJBubKSnp8t0IWsIhoaGGDRoEL777jsYGxtj7NixeO+99zBlyhTo6ekhJSUFenp6dRorjuPw9OlTdOvWTSXxKIq7uzsKCwtx//59pU0mnXfstCTtbGxs6mxewXEcsrOz5WZLny8f69KlCwCaY8WCps63oqIi0RurlnStqhrSTnnEppnSzSv09PQwbdo0XL16VR3xEM/x119/aToEUUK6sZGWloacnByV7W/QoEEAqief7t27F7NmzYKenh4AQCKRwM7Ork5jtXPnTsTFxWHSpEkqi0cR+M6A4eHhSmes6LxjpyVpZ2FhIazB+DzFxcUoKyuTm7F6nn/++QcAZaxY0NT5VlhYKPpSwJZ0raoa0k55xKaZ0sZKIpEIi2gS6oc6L7JBurGhyjlWAPDmm2/iypUrGDVqlNzX6zJW+fn5eP/99zF9+nQMGDBAZfEogpubm9CFUNk5VnTesdOStDMyMhLabj9PdnY2AMXOPf48JWOlPJo635pDxqolXauqhrRTHrFpxtRu/eOPP8avv/6K6OhoVcdDEISKkEqleOeddxAbG6vQ9hzHqdxY6evrw9/fv87X6zJWX331FfLz87FmzRqVxaIo+vr6wo28LkNIEA3B2NgYZWVlckv4srKyAEChjBVfGkjGSjxQ8wqCaN4wNa+4du0arK2t4enpiYEDB8ptty6RSPDzzz+rJMiWjLu7u6ZDECWkGxAdHY3169ejTZs2WL58eb3bJycno6ysDD4+Po0QXTW2trZ4+vSpzFh0dDR++uknfP7553BxcWm0WGryxhtvoLCwEIMHD1bqfXTesdOStOPXMCouLq71IIM3VopkrPiyVZpjpTyaOt8KCwuFdvlipSVdq6qGtFMesWnGZKx+/fVX4ftz587J3YaMlWro37+/pkMQJaQbcP36dQBAXFycQts/evQIABp1TpOdnR3Cw8Nlxg4fPgwjIyO8++67jRbH8/Bt4ZWFzjt2WpJ2fClYUVGRjLG6c+eO8BBEkYwVnw2mjJXyaOp8aw4Zq5Z0raoa0k55xKYZUymgVCqt94ueoKkGfnIyoRykW3VmGYDCpYCPHj2CtrY27ty5o86wZJBXCpiUlIQ2bdrAwMCg0eJQFXTesdOStOONVXFxscz4okWL8O+//wIAzM3N693PiRMnAJCxYkEV5xuL7s1hjlVLulZVDWmnPGLTjMlYEY1Hbm6upkMQJaTbf8ZKmYyVq6trnZPq1YGdnR2ys7NRUVEhjCUlJalsLa3Ghs47dlqSdnwp4PPXWs0sFd+Y4kUUFBQAIGPFQkPPN47j4Obmhh49eqCwsFAYLywsfOGD5eawjlVLulZVDWmnPGLTrEHG6tq1a/j222/x9ttvIyYmBkD1E7jbt2/L3GgIgmhcioqKEBkZiY4dOyIuLk6hrjqPHj1q9FpmOzs7AJDpMpqcnAxnZ+dGjYMgGpOapYA8WVlZKCsrU2o/WlrVf8KpQqTxyczMRGJiIsLDwzFx4kRMnToVbm5uMDU1fWEZc3MoBSQIom6YjFV5eTkmT56Mfv36YdWqVfjll1+ECehaWloYPnw4za9SEfb29poOQZS0dN1u3boFqVSKl156CUVFRXUuRloT3lg1pna8sapZDijmjFVLP+8aQkvSrmbzigcPHmD06NGwsbFBSEgIAGDWrFkK7YdvgkAZK+XR19fHm2++idLSUqb3P3z4EADwxRdf4OLFi0hOTsbEiRPh6+uLBw8e1Pm+5pCxaknXqqoh7ZRHbJoxGatPP/0Ux48fx6ZNmxAdHS3zNNzAwADTpk1DYGCgyoJsyYwdO1bTIYiSlqrb+fPn8cYbb+DatWswMTHBmDFjANRdDpiXl4cLFy6goqICsbGxcHd3b1TtnjdWUqkUKSkpos1YtdTzThW0JO34D9bffvstvL29ER0dDV1dXQDAH3/8gd27dyu0n/Hjx0MikajVWFVUVCApKUlt+9cUWVlZ+PXXXxEUFMT0/ocPH0JLSwsffPABCgoKcPXqVaxduxb9+/fHs2fP5L6nqqoKZWVlojdWLelaVTWknfKITTMmY7Vnzx688cYbWLx4sdzORR4eHgpPmCdezNmzZzUdgihpqbr973//w++//45z587Bz88P7du3B/5fe/cdFsW5tgH8XnqviiAIAlYioihgQcSK2HsltqiJUXPSkxNNTFdjouckMcZjwd4jFiwoGkUUO3ZURBEboEiTLjvfH3w7YYWFnZdld2f3+V0X1wUzu7Mvt7Mjz75loLiw6tWrF3r27Il79+7h1atXaNGihVqza9iwIYB/CqvMzEyUl5eLtsdKX887VdCn7GR/WMfGxiI8PBw3b97kby3g7u6u9HFiY2NhZGRUr4VVv3794ObmVuvjXrx4AR8fH5w/f77e2qJKsuJ1+/btTM9PSkqCt7c3TE1N5W434+bmprCwKioqAvBPj6VY6dN7VdUoO+HElhlTYZWZmQlfX1+F+w0NDausdkTYPHjwQNNNECV9zI3jOBw7dgxAxYWoU6dOsLW1hb29fbUfdJSXl/NLnZ87dw5Axf0i1JmdpaUlLC0t+cLqyZMnACDawkofzztV0afsKv9h3b59e5iamvKFlZB7tz148ABGRkb1NseqvLycv6bUJjExEUlJSZg4cWK9tEWVSkpKcPnyZbi6umLfvn1yf6+UlZVh165dtc5LvXHjBlq1alVlu5ubG/Lz85GXl1ft6wIVwxDFTJ/eq6pG2QkntsyYCqsmTZrw44urc+rUKf6TckKIety4cYMvUDiOQ1BQEADAy8ur2h6rhIQE/vuTJ0/C3NxcI0PwKi+5LvbCihBlGBoawsTEBADQoEEDABVzdRwcHODp6Sn4WPXVY3XixAn++9oKDdmHN7du3cLt27frpT2qcv/+fZSWluKbb75BYWGh3HDAqKgojBgxgr8PYHWOHj2Kw4cPIzw8vMo+We9edcMnZfO5xHgrCUKIcpgKq/Hjx2PFihVyf5jJloZduXIltm/fLopPrcSALsBs9DG3a9euAQCcnZ0BgC+sPD09qy2s0tLS+O/j4+PRvHlzGBgYqD27yoVVRkYGv02M9PG8UxV9zU5WWHXv3h1ZWVmChomZmZnV61DAyr1VtS3ykJycDBcXF1hbW2Pbtm310h5Vyc7OBlBxjWzfvj127NjB7/v7778BAHFxcQqfO3nyZPTo0QNvv/12lf2yD6eqGw6oKz1W+vpeVQXKTjixZcZUWM2dOxddunRBSEgIevToAYlEgg8++ADu7u54++230a9fP3zwwQeqbqtemjBhgqabIEr6mFt+fj4MDAzQqVMneHh48AWWp6dntUMBX7x4wX+flJTEL7Wu7uwqF1aZmZlwdHSEkZGRWtugKvp43qmKvmVXWloK4J95hiwmTJhQr4WVbJVCoOrNjF939+5d+Pr6YujQoVi3bp3CeUbaQFZY2dvbY/To0YiOjuaXvj9+/DgAxYXV7NmzkZ+fj7Vr1/LL3Vcm623X5R4rfXuvqhJlJ5zYMmMqrExMTHDo0CFERkbCy8sLrVq1QklJCdq2bYu1a9di3759MDQ0VHVb9ZJYJgJrG33MLS8vD1ZWVpg/fz5WrlzJb/fy8kJaWlqVP76ysrLg7OzMD0mSFVbqzu71wkqsvVWAfp53qqKv2cl6rFicP38ehoaG9TLHqrS0FGfPnkWfPn0AKFdYNWvWDB999BGKiorQt29fpe6fpwmyG47a29tj1KhR/HDAp0+f4tatW2jTpg3i4+PlblwOADExMdi8eTOWLVumcJERU1NTODk5yY0IkNGVHit9fa+qAmUnnNgyY75BsEQiQUREBHbv3o0bN24gKSkJ0dHRmDhxolJ3jCfKuXr1qqabIEr6mFt+fj6sra3Rrl07/o8hoKLHqry8vMonyC9evICjoyNfyMgKK3Vn9/pQQDEXVvp43qmKvmZXl8Lq6tWr9dZjde7cORQXF6Nv374Aai6sOI5DSkoKvL294efnh40bNyIpKQlnzpxRebtUITs7G0ZGRjA3N4e3tzc6dOiA7du383PKFi9ejNzc3Cqrke3evRvNmzfH+PHjazy+l5dXtaMEdKXHSl/fq6pA2QkntsyYCytCiHaRFVavk02Gf/0/+qysrGoLK3V7vcdKbDcDJKQu6lJYAai3wiomJgYODg7o1q0bgH+WCq9Ofn4+CgsL+YUbQkND4ebmhg0bNqi8XaqQnZ0Nc3Nz/kPg0aNHY//+/YiOjkarVq0QFhaG1q1bY+PGjXLPO3bsGHr16lXrh8fe3t5ISUmpsl1XeqwIIYopNZGhR48eMDAwQExMDIyMjNCzZ89anyORSHD06NE6N5AQohxFhZWHhwckEkmVBSxevHgBBwcHfrK8JgurwsJCFBQUIDMzE61bt9ZIOwjRhMr3QGJRX4XVoUOH0LdvX1hZWQGoucdKNl9Tdl9LAwMDREREYMWKFVi6dKnWFRI5OTlyN+kdNWoUPvvsM2zatAnvvPMOJBIJJkyYgB9//BEvX75EcXExGjdujLKyMnz//fe1Ht/Ly6vaZep1pceKEKKYUj1WHMdBKpXyP0ulUnAcV+NX5ccTdhEREZpugijpY26KCitTU1O4urpWKaxkPVaNGjWCg4MDHB0dAag/O1mPWWZmpujnWOnjeacqlJ1wERER9TLHat26dbhw4QIGDhzIf/BSU2GVlZUFAPw1BADefPNNZGdnyy1lri2ys7Ph4eHB/+zp6YnBgwejRYsWePPNNwFUrH5cWFiIPXv24NChQygrK0P37t0RFhZW6/G9vb3x9OnTKpnpSo8VvVfZUXbCiS0zpXqsZKvkKPqZ1J+0tDQ0b95c080QHX3MTVFhBVS/MqCsxyogIEBu+J26s5MVUunp6Xj27JmoCyt9PO9UhbITLi0tTeU9VsuWLcPs2bMxffp0jB07Fs+fPwdQ81DA13usAMDHxwf+/v5Yv349hg0bprL2qUJ2dja/aI/Mnj175H729PRE165dsWnTJtjb28Pf31/pv328vb0BVAy/btOmDb9dVliJvceK3qvsKDvhxJYZzbHScoqWfCU108fcaiusFPVYjRo1CosWLeK3qzs7WSGVlJQEqVQq6sJKH887VdG37K5du4aTJ0/W6RhxcXEqLaxWrlyJ2bNn46OPPsKKFStgaGjI3GMFABMnTsT+/fv5/doiOzubL3JqMmHCBBw+fBjR0dHV3gxYEVlhdffuXbntsqGAYu+x0rf3qipRdsKJLTOmwio2NhZffPGFwv1z586tdnwxIaT+1FRYvb5KVXl5OXJycuQ+YdYU2eR92co/tHgF0Qdt2rRBcHBwnY+jqsKK4zgsXrwYY8aMweLFi/kFGmRzwGqbY2VsbCw3bwkAxo0bh/Ly8iq9QZr2+hwrRUaNGgWJRAKO4/Duu+8qfXxnZ2c4ODjgypUrcttLSkogkUhgbGwsuM2EEHFgKqy+++47PHz4UOH+x48fKzXBkxCiOvn5+bCxsal2n5eXFzIzM/Hy5UsAFX9YcBxX5RNmTTAyMoKjoyMuXLgAAArvD0MIqUpVc6yuXr2K5ORkTJo0SW7VOyMjIxgbG9faY+Xo6FhltTwnJyd4eXnh+vXrdW6fKslWBaxNgwYN8PXXX2PlypX8jX+VIZFI0LFjR/6aJlNcXAxTU1O6JQ0hOoypsLp27RqCgoIU7g8ICBDduvPaauDAgZpugijpY2419Vg1a9YMwD9LrstuXtmwYcMqj9VEdk2aNMGFCxdgaGgIFxcXtb++qujjeacqlJ1wAwcOVFmP1cGDB2FtbY1evXpV2WdhYVHrHCtFvd+tW7fGrVu36tw+VcrOzkbHjh2VeuzcuXMxZswYwa8REBCACxcuyN0kuaSkRPTDAAF6r9YFZSec2DJjKqxKSkpQWlpa4/7a7tJOCFGtmgqr18f87927F9bW1ggMDFRb+2rSokULlJSUwNXVFYaGhppuDiGioarC6smTJ/Dw8KiyqANQUVgp02NVnVatWiEpKanO7VOV0tJS5OXlwd7evl5fp2PHjkhPT8fjx4/5bcXFxaJfuIIQUjOmwqpNmzaIioqqdh/Hcdi1axd8fHzq1DBSITo6WtNNECV9y+3Vq1coKipSWFg1bNgQ1tbWSElJQWlpKbZv347BgwdX++mpJrKT3UNL7MMA9e28UyXKTrjo6GiVFVbPnj1TeLNic3PzWudYKeqxatWqFR48eKA1H7Y+evQIwD+99vVFdk178OABv01XeqzovcqOshNObJkxFVZz5szBqVOnMGrUKFy7dg2vXr3Cq1evcPXqVYwaNQoJCQmYM2eOqttKCFEgPz8fABQWVhKJBN7e3jh27Bi6dOmCO3fuYNq0aepsYo10pbAiRN1UNcfq+fPn1Q4NBmofClhbjxXHcbhz506d26gKsvnh9b1wj62tLQAgNzeX30Y9VoToPqXuY/W6iIgIpKSk4LvvvsOuXbtgYFBRn0mlUkgkEsybNw+TJk1SaUMJIYrVVlgBFfOsdu7ciRYtWuDMmTPo0KGDuppXKyqsCGGjyh4rRfeKqW0oYE09VrIb8T569Ajt2rWrczvrSpOFla70WBFCFGMqrABg/vz5iIiIQFRUFD8h3tvbG0OHDuXnc5C6CwkJ0XQTREnfclOmsJo2bRqaNWuGefPm1bjUsCaykxVWsj/CxErfzjtVouyECwkJwe7du1VSWNXWY8U6x0o2l6lygaFJDx8+hIODA/r06VOvr2NpaQlDQ0Od7LGi9yo7yk44sWXGXFgBFYXUxx9/rKq2kGrQJ/hs9C032TCdmpYQDgsLQ1hYWK3H0kR29vb22Lt3L7p3767211YlfTvvVImyE87d3R2GhoYoKyur03E4jmOeYyWVSpGdna2wB8jc3BzGxsbIzs6uUxtV5eHDh2jSpEm9n28SiQQ2NjY62WNF71V2lJ1wYsuMaY4VUZ+NGzdqugmipG+5yf6wqm5FL6E0ld2gQYMU3odLLPTtvFMlyk64jRs3wsjIqM5zrF6+fInS0lKmOVa5ubmQSqUKe6wkEgns7e2Rk5NTpzaqSlpaGpo0aaKW883W1lYne6zovcqOshNObJlRYUWIDpDd/kAVhRUhRDxUMcfq2bNnAKCwx6qmoYBZWVkAap6zZGdnpzWFlazHSh1sbW2Rl5fH/6wrPVaEEMWosCJEB8h6rIyNjTXcEkKIOqmisHr+/DmA6m8YDlQM1ZUVX6978eIFACjssQK0p7AqLi5GUlIS3njjDbW83utDAXWlx4oQohgVVlqubdu2mm6CKOlbbqrssdK37FSJsmNH2QnXtm1bGBoa1nuPVbNmzXDv3r1qhxyKqcfq0qVLKCsrQ+fOndVyvr0+FFBXeqzovcqOshNObJlRYaXlAgICNN0EUdK33FQ5x0rfslMlyo4dZSdcQECASuZYyYojRb1OzZo1Q2lpKR4/flxlnzI9VqxzrIqLi/H06VPBz1MkISEB5ubm8PX1Vcv5Vl1hpQs9VvReZUfZCSe2zOpUWJWUlCAhIQF79uzhhxIQ1dq0aZOmmyBK+pabrMdKFUMB9S07VaLs2FF2wm3atEklQwFzcnJgZmam8I/+Zs2aAQDu3r1bZV9WVhbMzMxqXJHUzs6OaVXA//znP/Dz80NJSYng51YnISEBAQEBMDY2Vsv5Vt3iFbrQY0XvVXaUnXBiy4y5sPr111/h4uKC4OBgDB8+HFevXgVQMVa7QYMGWLNmjcoaqc+Ki4s13QRR0rfcVNljpW/ZqRJlx46yE664uFhlhZWdnZ3C/R4eHjA0NKy2sHrx4kWNvVWA8KGAR44cQXFxMe7du4dnz57hwIEDSj+3JmfOnEHnzp0BqOd8q1xYbdq0CYmJiTrRY0XvVXaUnXBiy4ypsIqMjMT777+Pfv36YfXq1eA4jt/XoEED9OzZE1u3blVZIwkhNVNljxUhRDxUMceqtsLKxMQE7u7uCnusappfBQgrrFJTU9G3b1+MGDECGRkZAID169cr9dyaPHz4EI8fP+YLK3WQFVYrVqxAREQEAKh0aCMhRPswFVa//PILhgwZgs2bN2PQoEFV9nfo0AE3btyoc+NIxSeFRDh9y620tBQSiQSGhoZ1Ppa+ZadKlB07yk44Dw8PtfRYARXDAevaY1X5Q1hFLl68CAA4cOAAzpw5AzMzM+zfvx+ZmZn4/PPP8eTJk1qPUZ2EhAQAQKdOnQCo53yzsbFBdnY2Zs6ciRkzZsDW1hb9+vWr99etb/ReZUfZCSe2zJgKq7t37yI8PFzhfgcHB34yLKmb3r17a7oJoqRvuZWVlcHY2BgSiaTOx9K37FSJsmNH2QnXu3dvGBsb80OBFeE4DpGRkQp7jepSWCnTY2Vvbw+pVIqXL1/W+DgASExM5L/PzMxEREQEOI7Dhx9+iEWLFmHJkiW1HqM6Z86cgaenJxo1agRAPeebLNMJEyZg+fLlyMnJwaRJk+r9desbvVfZUXbCiS0zpsLKzs6uxsUqbt68CWdnZ+ZGkX9ER0drugmipG+5lZaWquzmwPqWnSpRduwoO+Gio6NhYmJSa2F148YNTJ06FYGBgZBKpVX2CymsXu91UqbHSlZ4PXr0qMbHARWFVb9+/fjFMHx9fREeHs5PYK/ttRRJSEiQGwaojvMtLCwMv/76K9asWQMDA91ZhJneq+woO+HElhnTO71///743//+V+2nXzdu3MDKlSsxePBgwcddsGABAgICYG1tDScnJwwdOhS3b9+We0xxcTFmzZoFR0dHWFlZyY3DlklLS8OAAQNgYWEBJycnfPLJJ3UeKqEpr/9uRDn6lpusx0oV9C07VaLs2FF2wmVkZMDY2JifY6nI+fPnAQDJycm4c+dOlf3KFlZFRUVV5ggp02PVpUsX2NjYYMOGDTU+Li0tDWfOnEGHDh3g5eUFAHB2dsbEiRP5x+Tn59d4DJmLFy8iKysLf/75J7Kzs3Hp0iV+GCCgnvPNwcEBc+bM0bm5r/ReZUfZCSe2zJgKq++//x7l5eVo06YN5s2bB4lEgnXr1iEiIgIdO3aEk5MTvvrqK8HHPXHiBGbNmoUzZ87gyJEjKCsrQ9++fVFQUMA/5oMPPsC+ffuwY8cOnDhxAk+ePMHw4cP5/eXl5RgwYABKS0tx+vRprFu3DmvXrmVqDyFiocoeK0KIeCgzFFBWWAGodjhebm6uUoUVAKSkpMhtV6bHytLSEpMnT65xteA7d+4gODgYNjY2mDFjBry9vQEAjRo1wsCBA9GwYUMAqPXWLteuXUN4eDg6duyInj17YubMmejVqxdKS0vVunAFIUQ/MRVWjRs3xsWLF9GvXz9s27YNHMdhw4YN2LdvH8aNG4czZ84ovIN7TQ4dOoTJkyfjjTfegJ+fH9auXYu0tDR+Mmtubi5Wr16NJUuWoGfPnujQoQMiIyNx+vRpnDlzBgBw+PBh3Lx5Exs3bkS7du0QHh6O7777DsuWLav1Uz1tVNt/dqR6+pabKnus9C07VaLs2FF2wtnZ2SlVWJ07d47vrSksLKyyPycnB7a2tjUew8vLCxKJRG6e1atXr5CTk1NrjxVQsahVRkZGtf8P37x5E926dYOVlRXi4+Ph7u7OF3KNGjWCmZkZkpKS0KtXrxoLq/3796Ndu3a4e/cuOnfuzN8GJjExEfb29vDz8+MfS+cbO8qOHWUnnNgyYx706+TkhFWrVuHFixfIyMjA06dPkZ2djTVr1sDJyUkljZPd/0F20b548SLKysrkJrK1atUK7u7u/Io/CQkJ8PX15SeoAhXjnPPy8hSuVFhSUoK8vDy5L20xYsQITTdBlPQtN1X2WOlbdqpE2bGj7IQbMWJErYVVSUkJrl69itDQUABAUVGR3H6O45QaCmhmZgY3Nze5wko2HUCZeU9WVlYA5HvMpFIpbt26hW+++QbW1taIi4uDq6srgH96yGTztR0dHeHi4lLjwlhHjhyBp6cnbty4gXfffRcAEBoaiuXLl+PMmTNyHz7R+caOsmNH2QkntsyMVHEQWRe9KkmlUrz//vvo2rUr2rRpAwBIT0+HiYlJlf8AGjVqhPT0dP4xlYsq2X7ZvuosWLAA33zzTZXt69ev5yfQjhs3Dk+fPsXx48f5/f3794exsTH27NnDb+vatSu8vb3l7rvRpk0bBAUFYevWrfywRjc3N4SFheHgwYP88rE2NjYYNWoUTp8+jaSkJABAXl4e/vWvfyEpKYnvlQOA4cOHo6CgADExMfy2Xr16wdHREdu3b+e3dezYEX5+foiMjOQnLTdv3hwhISGIiorCixcvAFQUyoMGDcLRo0eRmpoKADA1NUVERAQuXryIy5cv88ccP348Hj9+jBMnTvDbBgwYAENDQ+zdu5ffFhwcDE9PT7lx9b6+vggMDMSWLVv4T07d3d3Rp08f7N+/n/83srW1xciRIxEfHy83z+6tt97CtWvXcO7cOX7byJEjkZeXh8OHD/PbnJyc0L17d+zYsYPfFhAQgLZt22LNmjX8BOwWLVqgW7du+Ouvv/g/EmRDT2JjY/HgwQMAFX9UTJgwAefPn+c/BQWAiIgIpKWlIS4ujt82cOBAAPITLkNCQuDu7o6NGzfy29q2bYuAgABs2rSJvwGeh4cHevfujejoaH5csZ2dHUaMGIGTJ0/y8yMkEgmmTp2Kq1ev4vz587h06RIKCwuRl5eH7OxsxMbG8q/Tt29f2NjYYOfOnfy2wMBA+Pr6YvXq1fy2li1bIjg4GMuXL+eLNGdnZwwYMABHjhxBWloaAMDCwgLjxo3DuXPncO3aNf75b775Ju7fv4/4+Hh+2+DBg1FeXo79+/fz27p37w5XV1ds3ryZ39auXTt06NABGzduRElJCQCgadOm6NWrF/bt24fMzEwAFR+yDBs2DHFxcUhOTgYAGBgYYMqUKbhy5QouXLjAH3P06NHIysrC0aNH+W1hYWGwtLTErl27+G2dOnVC69atERkZyW9r3bo1unTpgh07dvAftDRu3Bjh4eGIiYnhJ+FbWlpi7NixOHv2LK5fv468vDzY2Nhg4sSJSElJwalTp/hjDhkyBGVlZXI3Ow0NDYWLiwu2bNnCb2vfvj38/f2xfv16/g9mLy8v9OjRA3v27OE/sXd0dMTQoUNx/PhxfniWkZERJk2ahMTERFy6dIk/5tixY5GZmYljx47x22QLBERFRfHbOnfujJYtW2Lt2rX8Nh8fH3Tu3Bnbtm3j/yh2dXVFv379cOjQITx+/BhAxR/OY8aMQUJCAm7evMk/f/Lkybh9+zb/4RcADBs2DEVFRTh06BC/rUGDBujdu7fcPRD9/f3Rvn17rFu3jp8n6+3tjdDQUOzevZv/I7tBgwYYMmQI/v77b9y7dw9AxRC5iRMn4tKlS3IrzWnqWg4AU6ZMUem13NjYGCYmJigpKeHfy69fy+/du4eysjJ0794dCxcuxN69e/nzd/z48bh9+zakUikSExOxevXqGq/llpaWOHz4MLy8vODr68v3ciUkJCArK6vGa7nsWrpq1So4Ojpi4sSJCAkJ4bMYPnw4jI2N8fDhQxw+fBivXr3CW2+9hdzcXBgYGGDHjh1IT0/H3bt3cfXq1Wqv5SkpKbC1tcWGDRuQnZ0NAAgPD0ezZs1w8uRJnDx5kr+WV/4/CNCea7nMqFGj6nwt37lzJ/8BtSqv5bLrnC5fy2VUfS2XXaN1+Vres2dPODk5qexaXlBQgPfee08rruVvvfUWaiPhlLixxLffflvrgaocWCLBl19+Kfh5MjNnzsTBgwcRHx8PNzc3AMDmzZsxZcoU/s0qExgYiB49emDRokWYMWMGHjx4IPefVGFhISwtLXHgwIFql4kvKSmRO2ZeXh6aNGmC3Nxc2NjYMP8OqrB69Wql/iGJPH3L7b333sPx48flij5W+padKlF27Cg74VavXg2O4zB9+nRIpdJqb7ewbNkyfPDBB8jMzIS9vT02btyICRMm8PsfPnwId3d3HDx4sNZ7LM2YMQMXL17kh+cnJCSgS5cuuH79Ot54440an3vmzBl07twZ165dQ5s2bXDy5EmEhITAwsIChYWFSE5O5nupFPnhhx/w66+/KpzM7uPjgz59+uC///0vACAqKgo9e/asdpgjnW/sKDt2lJ1wYstMqR6rr7/+uso22QX89bpMIpGA47g6FVazZ89GdHQ04uLi+KIKqPjEpbS0tMqwhYyMDH64gLOzs1xvhmy/bF91TE1NYWpqytRWQrSBKudYEULEQ/a+Lysrq3Y48Pnz59G2bVu+uHh9jpWsp16ZeQzNmjXj51VLJBL+U2Zl5ljJhgLKVvU7ceIEbG1tcefOHcTFxdVaVAEVn2ZnZWVBKpVWWb5cKpXi3r17/KIXQMWn6YQQok5KzbGSSqVyXw8fPoSvry/fhZybm4vc3FycPXsWY8eOhZ+fHx4+fCi4MRzHYfbs2YiKisKxY8fg6ekpt79Dhw4wNjaW6w6+ffs20tLS+NV+ZJ+IybqbgYpx1zY2NvDx8RHcJk1TxQ1f9ZG+5abKOVb6lp0qUXbsKDvhJBKJXGFVnfPnzyMgIAASiYTvHapMNlRMmdEZzZo1Q15eHj+ESTaUXJnCytraGsA/c6xOnDiB4OBgODk5YeTIkbU+H6gYMlVeXo7+/fujvLxcbt+TJ09QUlIiV1jVhM43dpQdO8pOOLFlxrR4xaxZs9C8eXNs3LgRHTt2hLW1Naytrfkxxt7e3pg1axbTcTdu3IjNmzfD2toa6enpSE9P5yfb2tra4q233sKHH36Iv//+GxcvXsSUKVPQuXNnfsWjvn37wsfHB2+++SauXLmCmJgYzJs3D7NmzRJlr9TUqVM13QRR0rfcVNljpW/ZqRJlx46yE27q1Kn8ByrVFVb5+flISkpCQEAAAFRbWMnmF8h6lGoi61WSLWCRlZUFS0tLpf5vlRVW+fn5KCsrw+nTpxESElLr8yqTLZIRExPDzweRkc1Nkd3/qjZ0vrGj7NhRdsKJLTOmwurYsWPo2bOnwv29evWS61VS1vLly5Gbm8tPApR9bdu2jX/M0qVLMXDgQIwYMQIhISFwdnaWm7xoaGiI6OhoGBoaonPnzoiIiMDEiROZ5olpA1XMmdFH+pabKnus9C07VaLs2FF2wl29epX/QKXyMuYrVqyARCLBxYsXwXGcXGH1+qqAsh4kZQorb29vGBkZ4a+//gKg3D2sZCoPBbx48SIKCwvRvXt3pZ4r4+fnxxdOskUHNm3ahOTkZKSkpEAikVQZ6aIInW/sKDt2lJ1wYsuMqbAyMzOTWxXkdadPn4aZmZng43IcV+3X5MmT5V572bJlePHiBQoKCrBr164qc6c8PDxw4MABFBYW4tmzZ/j5559hZKSSBRDVrvIqQUR5+pabKgsrfctOlSg7dpSdcOfPn692KOC6desAAKdOnYKFhQVat24NADA3N6/SYyWksLK0tMQPP/yAX375BdevX8ejR4+UvmeliYkJTExM8PLlS8TFxcHS0hL+/v5KPVfGwcGBXyHt0aNHuHPnDt58802sWrUKKSkpcHV1VfpvDzrf2FF27Cg74cSWGVNhNWHCBGzatAnvvfcekpOT+blXycnJmDNnDjZv3iy36hAhpH7R4hWE6KfqCivZ0LzTp0+jXbt2/AeLioYCypZtV8bbb78NALh27RpiY2MFDeezsrJCfn4+Tpw4gS5dujBds2xsbGBlZYVHjx7hl19+AcdxePToEVJSUpSeX0UIIfWFqRtn0aJFeP78OX7//XcsW7aMX51HKpWC4ziMGzcOixYtUmlDCSGKlZaWavzWAIQQ9auusJIVSU+fPoWHhwe/vbrC6uXLl0r1VsnY2trCwcEBe/bswaNHjzBgwACln2ttbY2cnBzEx8fjk08+Ufp5lUkkEri5ueHixYv466+/YGxsjMePH6OgoABt27ZlOiYhhKgKU2FlYmKCDRs24JNPPsGBAwf4G/95eHggPDwcfn5+Km2kPhs1apSmmyBK+pabKnus9C07VaLs2FF2wo0aNYq/mWnlOVaywiorK4sfBggoLqwsLS0Fva63tze2bdsGS0tLdOvWTennWVtb49SpU8jLyxM8v6oyNzc3bNmyBZaWlhg3bhyOHTuGFy9eCFpenc43dpQdO8pOOLFlVqeJR23btqVPiOpZdnY29UQw0LfcVDnHSt+yUyXKjh1lJ1x2dnaNPVZZWVmwsLDgt1tYWODIkSP44YcfMHfuXADCe6yAipX3zp8/j65duwpabdfKygqnT5+Gqakpv6AGCzc3N/7GyE2bNsXKlSsBQNBQQDrf2FF27Cg74cSWGdMcK6I+sbGxmm6CKOlbbqrssdK37FSJsmNH2QkXGxtb4xyrgoICucLK3NwcOTk5+PLLL5GRkcE/RmhhJRteKLTXydraGlKpFJ06dWJa4ErG3d0dRkZGeP/99+Hm5sZvb9WqldLHoPONHWXHjrITTmyZUWFFiEidPn0a0dHRAFTbY0UIEY+aeqwAVOmxAipW4N27dy8Ath6rV69eAQB//0hlye5lJfT+Va979913ERMTA3d3d7nCikbQEEI0TZxrkBNC8NNPP+HKlSsYOHAgrQpIiJ5iKawAICoqCtOnT2cqrN5//33k5uYiODhY0PNkr1OX+VUA0KhRIzRq1AgA4OrqCgBo3rw5JBJJnY5LCCF1RT1WWq5v376aboIo6UNuqampSE1NRVpamkp7rPQhu/pC2bGj7ITr27cv/76vbvEKoPrCytnZGUePHkVeXh7T4hVNmjTBqlWrBF9zrK2tYWRkhM6dOwt6Xk1cXFwwffp07Nu3T9Dz6HxjR9mxo+yEE1tmVFhpOTFN2NMmupxbamoqPv74Y9y7dw8AcPLkSZX2WOlydvWNsmNH2QlnY2MjqMdKdmuUd955B6WlpThw4ADTHCtW4eHh+Oijj+TaVFcGBgb43//+h5YtWwp6Hp1v7Cg7dpSdcGLLTGWFFcdxOHbsGA4ePIj8/HxVHVbv7dy5U9NNECVdzm3btm345Zdf+PfZyZMnVdpjpcvZ1TfKjh1lJ9zOnTsFFVbZ2dkAgK5du8Lf3x9RUVFMQwFZDRgwAAsXLlTLa9WGzjd2lB07yk44sWXGVFjNnTsXPXr04H/mOA59+/ZFnz59MGDAAPj6+iIlJUVljSSE/OPixYv89/7+/oiLi6M5VoToqeoKK47j+O8rF1ZZWVkAKobyDRs2DAcOHEBWVpbaCitCCNF1TIXVX3/9hcDAQP7nnTt34ujRo/j+++8RHR2N8vJyfP3116pqI1GBFy9e4MmTJ5puBlGByoXVm2++iaSkJGRnZ9OqgITooermWJWXl/PfVy6sGjduDKBiwYdhw4bh5cuXSE9Pp8KKEEJUhKmwevz4MZo1a8b/vGvXLvj4+ODf//43+vfvj5kzZ+L48eOqaqNeq1zA1kWPHj3g6uoq9x+uLlNVbtomOzubn1sFACNGjABQsfyxqnqsdDU7daDs2FF2wgUGBlbbYyWVSvnvKxdWCxcuxOnTp2FlZQUfHx80b94cAAQvXqEL6HxjR9mxo+yEE1tmTIWVkZERSkpKAFQMOTh69Cj69evH72/UqBGeP3+umhbqOV9f3zofg+M4XL16FQCwZ8+eOh9PDFSRm7bhOA5z5syBkZER9u7diz/++ANNmjSBp6cnAKisx0oXs1MXyo4dZSecr69vtYVV5Q/QKhdN5ubm/Ip8EokEw4YNAwC97LGi840dZceOshNObJkxFVZt2rTBxo0bkZ2djcjISGRlZWHAgAH8/gcPHqBBgwYqa6Q+W716dZ2PUbmHY/bs2Xjw4EGdj6ntVJGbtomOjsamTZuwfv16DBo0CDNnzgQAdOvWDQBU1mOli9mpC2XHjrITbvXq1ZBIJDA0NFRYWNW0Ap8+F1Z0vrGj7NhRdsKJLTOmwuqrr77C5cuX0aBBA0yfPh1du3aVW8xi//79CAgIUFkjSd2cPHkSEokEt27dQllZGf744w9NN4kIJJVK8dVXXyE0NBTjxo2T2xcSEgJAdT1WhBBxMTY2ZiqsgoKC8OeffyIsLKxe20cIIfrCiOVJffr0waVLl3DkyBHY2dlhzJgx/L7s7GyEhIRgyJAhKmskqZsdO3YgMDAQLVu2RFBQEK5du6bpJhGBoqKicPnyZcTFxVXZJyusTE1N1d0sQogWMDExUWrxitdJJBK8/fbb9do2QgjRJ0yFFQD4+PjAx8enynZ7e3ssXbq0To0i/xB608PXPXz4EIcOHcKKFSsAVAzj3Lx5syqaptXqmps2kUqlmD9/Pvr06cMP+6usWbNm2LJlC8LDw1XyerqUnbpRduwoO+FkmbH2WOkzOt/YUXbsKDvhxJYZc2EFAPfv38fBgwf5OTseHh4IDw/nJ9OTugsODq7T89euXQtzc3O+V9HX1xcPHz5Ebm4ubG1tVdFErVTX3NTl2bNnmD9/PpYsWQIzM7NqH7N9+3bcuHFD4ThjiUSCsWPHqqxNYslOG1F27Cg74WSZ1VRYmZubq71dYkDnGzvKjh1lJ5zYMmOaYwUAH330EZo3b47Zs2dj8eLFWLx4MWbPno3mzZvj448/VmUb9Vpd7jgtlUqxevVqjB07FtbW1gD+WV3l8uXLqmie1hLLnbp3796N5cuX4/Tp0wof88cff6BPnz4ICgpSS5vEkp02ouzYUXbCyTJTVFgZGxvTjcMVoPONHWXHjrITTmyZMRVWv/zyC5YuXYrhw4cjISEBOTk5yMnJQUJCAkaOHImlS5fScEAVyc3NZX5ubGwsHjx4gOnTp/PbWrVqBQ8PD4wePRpHjx5VRRO1Ul1yU6f4+HgAwPnz56vd/+zZM5w6dUpuHmN9E0t22oiyY0fZCSfLTNEcKxoGqBidb+woO3aUnXBiy4ypsFq5ciUGDx6M7du3IygoCDY2NrCxsUFQUBC2bt2KQYMG8XN6iOasWrUKbdq0kbu5momJCc6dO4e2bduiT58++OWXXzTYQnLq1CkAwLlz56rdHx0dDY7jMHDgQHU2ixAiIop6rKiwIoQQ9WIqrFJTU2tcnjUsLAypqamsbSKVODs7Mz2voKAAu3fvxtSpUyGRSOT2OTk54dChQ5gyZQrmz5+vimZqHdbc1Ony5ctISUmBl5eXwsJqz5496Ny5Mxo1aqS2dokhO21F2bGj7ISTZaaosLK3t9dIu8SAzjd2lB07yk44sWXGVFg5OTnhypUrCvdfuXIFDRs2ZG4U+UflGy8LkZaWhrKyMnTs2LHa/YaGhujRowcKCgpQWFhYlyZqJdbc1CUnJwcjR45Eu3bt8Omnn+LRo0coKSmRe0xhYSEOHz6s9lsXaHt22oyyY0fZCSfLrLrCqlOnToiKitJU07QenW/sKDt2lJ1wYsuMqbAaNWoUVq1ahYULF6KgoIDfXlBQgEWLFmHVqlVqnROiy44cOcL0vCdPngAAXF1dFT7GyckJQMU8Hl3Dmps6SKVSTJw4EVlZWfjrr7/g5uYGAMjKyuIfw3Ec1q9fj6KiIrUXVtqcnbaj7NhRdsLJMjM2Nq4yx6pBgwZo0aKFppqm9eh8Y0fZsaPshBNbZkzLrX/33Xe4fPkyvvjiC3z11Vdo3LgxgIo/5l+9eoUePXrg22+/VWlD9VVaWhrT8x4/fgwAcHFxUfgYWa9iZmYmPDw8mF5HW7HmVp/Ky8uxbt067Nq1C/v370d0dDS8vLyQmZkJAJg2bRpiYmIglUr550yZMkXt93DQxuzEgrJjR9kJJ8vMxMRErsdKKpXCyKhOd1PReXS+saPs2FF2woktM6Yrr4WFBY4ePYo9e/bI3ceqX79+6N+/PwYNGlRlXg9RrydPnsDBwaHGe5jICitd7LHSRpGRkZg+fToCAwOxfPlyvnu7QYMGAIDDhw8jMDAQU6dOhYGBAezt7dXeW0UIEZ/qhgKamJhosEWEEKKf6vSR1pAhQ+gPv3rGuqrT48eP+Z5ERXS5sNLG1bCuX7+OVq1a4ezZs3LbHR0dAVT8MRQcHCy3PL4maGN2YkHZsaPshJNlVl1hZWhoqKlmiQKdb+woO3aUnXBiy4z5BsFEPcaNG8f0vCdPntQ4vwoATE1NYWNjU21hderUKfj5+WHu3LngOI6pDZrEmlt9unfvHry8vKpst7W1hYFBxVuxpqGb6qKN2YkFZceOshNOlpm5ubncfGcqrGpH5xs7yo4dZSec2DJTqrDy9PSEt7c3/4mYp6cnvLy8avzy9vau14brC0XLcNdGmR4roKLXSjbHp7JffvkFV69exR9//AEXFxesXbuWqR2awppbfVJUWBkYGPC9VtpQWGljdmJB2bGj7ISTZebu7s4PyQeosFIGnW/sKDt2lJ1wYstMqcKqe/fuCAkJ4T9V7969e61fISEh9dpwfXHt2jWm5ynTYwVUFFbV9VhdvnwZ7dq1Q05ODjIyMvDvf/9b7hNRbceaW33hOE5hYQVAqworbctOTCg7dpSdcLLMvLy8kJqayi98Q4VV7eh8Y0fZsaPshBNbZkrNsXq9t0JsvRf6KCsri/9jvSbVFVY5OTm4f/8+Vq1ahffeew+tW7fG1atX8d///hdffPFFfTVZp2VkZKCoqEgUhRUhRFw8PT1RXFyM9PR0NG7cmAorQgjREJpjpYPKy8tRWFgIGxubWh/r5ORUpbC6evUqACAoKAhbtmzBpk2bMHPmTCxatEjuXktEeSkpKQBAhRUhROVk15X79+8DoB4rQgjRFKbCasuWLZg8ebLC/VOmTMH27dtZ20QqefPNNwU/5+XLlwAAa2vrWh9bXY9VXFwczMzM0LJlSwwePBgtW7bE3LlzIZVKsWDBAsHt0QSW3OrTqVOnYGFhofCGnQ0aNICFhYVS/2b1TduyExPKjh1lJ5wss6ZNmwKomMcJUGGlDDrf2FF27Cg74cSWGVNhtXTpUpiamircb25ujqVLlzI3ivxD9gmkEPn5+QCUL6wqL15RUFCAX3/9FRMnToSxsTG/3cnJCf/617/wxx9/oLy8XHCb1I0lt/oUExOD0NBQhe8bT09PtGjRQivu/6Zt2YkJZceOshNOlpmVlRWcnJyox0oAOt/YUXbsKDvhxJYZU2F1+/ZttG/fXuF+Pz8/3Lp1i7lR5B/x8fGCnyO0sCooKMAXX3yBEydOYPny5cjOzq52LlVwcDCKiorw8OFDwW1SN5bc6ktBQQHi4+MRFham8DGffPIJjh07psZWKaZN2YkNZceOshOucmaenp7UYyUAnW/sKDt2lJ1wYsuM6QbBHMchJydH4f7s7Gy5mxUS9RJSWDk5OQEAFixYgAULFqBhw4aYMmUKPDw8qjy2efPmAIDk5GR+6Amp3YkTJ1BaWlpjYWVqalpjLzAhhNTEy8uLeqwIIUTDmHqs2rdvjy1btqC0tLTKvpKSEmzevLnGHi2iGh999BFWrlxZZWheXl4eAOV7rCpT1FsFAB4eHjAyMkJycjJji/VTTEwM3N3dFc6vIoSQuqIeK0II0Tymwurzzz/H9evX0aNHD+zbtw/37t3DvXv3sHfvXoSGhuLGjRv4/PPPVd1WvdS8eXOcPXu2yvbc3Fz89ttv+Oijj+Do6Ig9e/bw+4QOBaxsypQpCnujjIyM4OXlhbt37wr4DTRj8ODBmm4CLyYmBmFhYVoxf0oZ2pSd2FB27Cg74Spn5uXlhcePH6OkpIQKKyXQ+caOsmNH2QkntsyYCqvw8HCsXr0a169fx9ChQ9G8eXM0b94cQ4cOxc2bN7Fy5UoMGDBA1W3VSz/++CPmzp0rt23x4sWws7NDWVkZysrKUFhYiE8//RSvXr0CwF5YLVmyBD/++GONj2/evLkoeqy0ZYGNBw8e4Pbt2zUOA9Q22pKdGFF27Cg74Spn5unpCY7j8ODBA0ilUhgY0N1UakLnGzvKjh1lJ5zYMmO+8k6ePBkPHz7Etm3b+Pk5O3bswKNHjzB16lRVtlGvWVpa4ty5c3In1urVq/nv7969i1OnTuHOnTv8jZvz8/NhbGys1JwdMzMzWFtbw8rKCu+//z4aNGhQ4+Nbt26NS5cuQSqVsv1CarJ//35NNwFARW+VoaEhevXqpemmKE1bshMjyo4dZSdc5cwq38uKeqxqR+cbO8qOHWUnnNgyY1q8QsbGxgYjR45UVVtINby8vJCfn4+kpCS0adMGHMchMzMTQ4YMwb///W+4urrC1dUV48aNw9dff40JEyYgPz9f0P2QGjZsCAsLC6WGqg0ePBg///wzEhIS0LVr1yr7b9++DQcHhypDDPXNihUrcP78eeTk5CAoKAh2dnaabhIhRIe5ubnB0NAQ9+7do8KKEEI0hLnHqry8HFu3bsXbb7+NYcOG4dq1awAq5v7s2rULGRkZKmukPmvatCkMDAxw5swZAEBKSgqys7PxzjvvICgoiH/ct99+i4yMDCxbtoypsKpuFcDqdO3aFa6urlixYgU4jquyf/jw4fjyyy+Vfm1dtWfPHmzYsAGxsbHo27evpptDCNFxRkZG8PDwoB4rQgjRIKYeq5ycHPTr1w/nzp2DlZUVCgoKMGfOHAAVNyp87733MHHixFrn65DahYWF8cPvAOD8+fMAgICAALnHNWvWDNOnT8eCBQswcOBA2NjYKP0a8+bNU7oQMzAwwJdffskXdrNmzeL3lZWV4c6dO1rRO9O9e3eNvv7NmzdRWlpa6zLr2kjT2YkZZceOshPu9cxkKwNSYVU7Ot/YUXbsKDvhxJYZ86qAN27cQExMDO7duyfXc2FoaIiRI0fiwIEDKmukPnN1dUWzZs34+5OcO3cOXl5ecHR0rPLYL7/8EkVFRVi/fr2gHquBAwcKOnHffvtthIWF4eDBg3LbU1NT8erVK9y8ebPa3ix1cnV1VdtrHT16FKdOneJ/fvnyJR48eAAAsLe3r1IEazt1ZqdrKDt2lJ1wr2cmu5cVFVa1o/ONHWXHjrITTmyZMRVWu3fvxpw5c9CnT59q5+W0aNECqampdW0bAbB582Z4enryhdX58+cV/qHu4uKCadOmAahY9KI+dezYke9Fk7lz5w6Aih7N9PT0en392mzevFltr/Xdd99h5MiRKCgoAAAkJSUBqFjoY/jw4aL7A0ed2ekayo4dZSfc65lRj5Xy6HxjR9mxo+yEE1tmTIVVbm4uPD09Fe4vKyvjl/4WIi4uDoMGDULjxo0hkUiwe/duuf0vX77E7Nmz4ebmBnNzc/j4+ODPP/+Ue0xxcTFmzZoFR0dHWFlZYcSIEaKf7yUrrEpLS3Hp0iUEBgYqfOzo0aMBVAxFq0/+/v54+vQpnj59ym+TFVaVX//p06dISEio17ZoWnFxMdLT07F06VIAFb2KQEURvHLlSk02jRCiR7y8vJCTk4OcnBwqrAghRAOYCitvb+8qvRWVHT58GD4+PoKPW1BQAD8/Pyxbtqza/R9++CEOHTqEjRs3IikpCe+//z5mz56NvXv38o/54IMPsG/fPuzYsQMnTpzAkydPMHz4cMFt0Saenp4oLS3F0aNHUVRUVOPQss6dOwOo/3X//f39AVQUwzJ37txBmzZtYGFhwQ8T/PHHHxEeHi66+xAIUVxcDCMjIyxatAhxcXH49NNPMWrUKFhaWormpsCEEPGr/IEnFVaEEKJ+TIXVtGnTsGbNGmzbto2fSyORSFBSUoK5c+fi0KFDePvttwUfNzw8HN9//z2GDRtW7f7Tp09j0qRJCA0NRdOmTTFjxgz4+fnxPQS5ublYvXo1lixZgp49e6JDhw6IjIzE6dOn+VX1xKZdu3b8f5bbt2+HgYEBX9RUx9DQEPHx8Th+/Hi9tsvDwwOBgYGYMGECPvnkE+Tn5yMmJgaBgYH497//jf/85z+4cOECzp49i9zcXCQmJtZre17Xrl07tb1WSUkJIiIiYGhoiPDwcDg4OPD3FBMjdWanayg7dpSdcK9n1rhxY/57KqxqRucbO8qOHWUnnOgy4xhIpVJu2rRpnEQi4ezt7TmJRMI5OztzxsbGnEQi4d555x2Ww8oBwEVFRcltmz59OtexY0fu0aNHnFQq5Y4dO8ZZWVlxJ06c4DiO444ePcoB4LKzs+We5+7uzi1ZskThaxUXF3O5ubn818OHDzkAXG5ubp1/D1V4+fIlB4AzNTXlfH19Nd0cXklJCffjjz9yZmZmnIODAweAO3XqFFdaWsr5+/tzPj4+nImJCQeAW7x4saabW2+aNm3KffHFF9yiRYs4ANyiRYs03SRCiB56/vw5B4ADwC1btkzTzSGEEL3DtNy6RCLBypUrMWnSJOzcuRPJycmQSqXw9vbG6NGjERISoqKyT95vv/2GGTNmwM3NDUZGRjAwMMDKlSv510tPT4eJiUmV5b4bNWpU42IKCxYswDfffFNl+/r162Fubg4AGDduHJ4+fSrXE9S/f38YGxtjz549/LauXbvC29sb69ev57e1adMGQUFB2Lp1K7/AgZubG7+y3pMnTwBU3HB51KhROH36NL8AwrNnz/Dpp5/Cx8cHN2/ehK2tLVavXo3hw4ejoKAAMTEx/Ov06tULjo6O2L59O7+tY8eO8PPzQ2RkJKRSKQCgefPmCAkJQVRUFF68eAEAcHJywqBBg3D06FF+4RFTU1NERETg4sWLuHz5Mn/M8ePH4/Hjxzhx4gScnJwwf/58HDt2DMXFxbh58yaSkpIwZMgQfP/99ygrK4O1tTXWrFkDe3t7+Pr6IjAwEFu2bEFhYSEAwN3dHX369MH+/fv5fydbW1uMHDkS8fHxuH37Nv/ab731Fq5du8b3UgLAyJEjkZeXh8OHD/PbpFIpxowZgx07dvDbAgIC0LZtW6xZs4bvaW3RogW6deuGv/76Czk5OQAqzpeBAwciNjaWX93PzMwMEyZMwPnz53H16lX+mBERESgsLMSNGzfQr18/jB8/HiNHjkRGRgaio6P5x4WEhMDd3R0bN27kt7Vt2xYBAQHYtGkTiouLAVT0BPbu3RvR0dH83EA7OzuMGDECJ0+e5OexSSQSTJ06FVevXuWX4AeAUaNGITs7G7Gxsfy2vn37wsbGBjt37uS3BQYGwtfXF6tXr+a3tWzZEsHBwfj5559hb28PAHB2dsaAAQNw5MgRpKWlAQAsLCwwbtw4nDt3jr9/HQC8+eabuH//PuLj4/ltgwcPRnl5udyd07t37w5XV1e5Cant2rVDhw4dsHHjRpSUlACouIdbr169sG/fPmRmZgIAHBwcMGzYMMTFxSE5ORlAxS0ApkyZgitXruDChQv8MUePHo2srCwcPXqU3xYWFgZLS0vs2rWL39apUye0bt0akZGR/LbWrVujS5cu2LFjB/Ly8gBU9AaEh4cjJiYGjx49AlCxSMzYsWNx9uxZXL9+Hc+ePUPDhg0xceJEpKSkyK0WOWTIEJSVlcmtmBoaGgoXFxds2bKF39a+fXv4+/tj/fr1KCsrA1Axd6ZHjx7Ys2cPnj9/DgBwdHTE0KFDcfz4caSkpACouJfRpEmTkJiYKDdce+zYscjMzMSxY8f4bf369YO5uTmioqL4bZ07d0bLli3lelx9fHzQuXNnbNu2DS9fvgRQsUpTv379cOjQITx+/BhAxa02xowZg4SEBLk5npMnT8bt27fl5loOGzYMRUVFOHToEL+tvLwcEyZMwNatW/lt/v7+aN++PdatW8fP2/X29kZoaCh2796NrKwsAECDBg0wZMgQ/P3337h37x4AwNjYGBMnTsSlS5fkesw1dS0HgClTpiApKUluBEVdruWFhYWYM2cOfy2XvXcAIDk5mX9/K3MtlxkwYAAMDQ3lhtgHBwfD09MTGzZs4Lep61reu3dv2Nvbq/xavmzZMpiZmfHHjIiIQFpamtzw9oEDBwKAaK/lO3fuRG5uLgDVXstl1zldvpbLqPpaXlBQgPfee0+nr+U9e/aEk5OTyq7lWVlZ+PTTT7XiWv7WW2+hVkIrsYKCAm7YsGHcxo0bVV/mVYJqeqwWL17MtWjRgtu7dy935coV7rfffuOsrKy4I0eOcBzHcZs2beJMTEyqHCsgIID79NNPFb6WNvdYrVq1iuM4jvvjjz84ANyCBQs03CLlLVq0iLOxseFWrFjBAeCuXbumtteW5aYO9vb2OtVLpc7sdA1lx46yE+71zMrLy/keq5UrV2qoVeJA5xs7yo4dZSec2DITPMfKwsICsbGx/CdU6lJUVIQvvvgCS5YswaBBg9C2bVvMnj0bY8aMwc8//wyg4hOZ0tJS/tMqmYyMDDg7Oys8tqmpKWxsbOS+tM2kSZMwbdo0TJo0SdNNUdqnn36KJ0+eYMqUKXB1dcUff/yh6SbVi5KSEpiammq6GYQQPWdgYMDPrTIwYJpCTQghpA6YrrzBwcFqX0K7rKwMZWVlVf6zMDQ05IdFdOjQAcbGxnLdxbdv30ZaWhq/Wp7YNG3aFEBFQbty5Uq4uLhotkECWVpawtjYGMOGDcOBAwfUduNgWW7qUFxcLDekROzUmZ2uoezYUXbCVZeZiYkJAFq8ojZ0vrGj7NhRdsKJLTMJx/CX7r179xAWFoYxY8bgnXfegZubm0oa8/LlS9y9exdAxdjUJUuWoEePHnBwcIC7uztCQ0Px/Plz/P777/Dw8MCJEycwc+ZMLFmyBDNnzgQAzJw5EwcOHMDatWthY2ODOXPmAKhYUVBZeXl5sLW1RW5urlb2XonR/v37MXDgQNy6dQstW7bUdHNU5tWrVzA2NkZkZCQmT56s6eYQQvScnZ0dcnNzsWHDBkRERGi6OYQQoleYeqz8/Pzw6NEjLFiwAB4eHtUOpbO1tRV83AsXLqB9+/Zo3749gIr7VrVv3x5fffUVAGDr1q0ICAjAhAkT4OPjg4ULF+KHH37AO++8wx9j6dKlGDhwIEaMGIGQkBA4OzvLTW4Um3379mm6CSoRGhoKY2NjHDlyRC2vp67cZBOVdanHSlfOOU2g7NhRdsJVl5mxsTEA6rGqDZ1v7Cg7dpSdcGLLjGlVwBEjRtTLjU9DQ0NrHCrm7Owst9pLdczMzLBs2TKFNxkWG9kKOmJnaWmJdu3aya0AVZ/UlZts1SNdmmOlK+ecJlB27Cg74arLjIYCKofON3aUHTvKTjixZcZUWIn55qdEczp06CC3lK1QRUVFKC0tZeoNrS+62GNFCBEv6rEihBDNETQUsLi4GNu2bcPChQuxatUqPH36tL7aRf6fg4ODppugMh06dMCtW7f4ewYINW/ePAwbNkypx6orN13ssdKlc07dKDt2lJ1w1WVGPVbKofONHWXHjrITTmyZKb14RWZmJrp06YL79+/zw/UsLCywe/du9O7du14bqW60eEX9SExMhL+/P+Lj49G1a1fBzw8LC0NaWprcDTc17ebNm3jjjTdw6tQpdOnSRdPNIYTouTfeeAM3b97E3r17MWjQIE03hxBC9IrSPVbfffcdUlNT8cEHHyA6Ohr/+c9/YG5ujrfffrs+26f36jJ0Ttu88cYbMDExwcWLF5men5qaqnRvl7py08UeK10659SNsmNH2QlXXWbUY6UcOt/YUXbsKDvhxJaZ0oXV4cOHMXHiRPz888/o378/3nvvPfz+++9ITU3F7du367ONei05OVnTTVAZExMTtG3bFhcuXBD8XI7jkJaWpvSNqdWVmy7OsdKlc07dKDt2lJ1w1WVGhZVy6HxjR9mxo+yEE1tmShdWaWlpCA4OltsWHBwMjuOQkZGh8oYR3dShQwemHqvMzEwUFxczz8+qL7rYY0UIES9avIIQQjRH6cKqpKSkyqfysp9fvXql2lYRnoEB063GtBbrAhapqakAKnqIysvLa328Mrnl5OSgqKhIUDtep4s9Vrp2zqkTZceOshOuusyox0o5dL6xo+zYUXbCiS0zQcutp6am4tKlS/zPubm5ACq66ezs7Ko83t/fv26tI5gyZYqmm6BSHTt2hFQqxeXLlwUtYPHgwQP++6KiIlhZWdX4eGVyCwsLQ2BgIH777Tel2/E6Xeyx0rVzTp0oO3aUnXDVZUY9Vsqh840dZceOshNObJkJKgO//PJLBAQE8F+y1QDfffddue0dO3ZEQEBAvTRY31y5ckXTTVAp1gUsZD1WAJTq7aott8LCQly4cAGxsbGC2vE6Xeyx0rVzTp0oO3aUnXDVZSbrsRLbp7zqRucbO8qOHWUnnNgyU7rHKjIysj7bQRS4cOEC/Pz8NN0MlZEtYCG0sKrcY6VMYVVbbleuXIFUKsWtW7fw7NkzNGzYUFB7ZHSxx0rXzjl1ouzYUXbCVZcZDQVUDp1v7Cg7dpSdcGLLTOnCatKkSfXZDqJHOnTogPj4eEHPefDgARo0aIDnz58rvTJgTS5cuAADAwNIpVKcOnUKQ4cOZTpOcXExJBIJP/yGEEI0iQorQgjRHBorQNTO398fSUlJfG+PMlJTU+Hj4wNAuR6r2ly6dAnt27eHu7u74CKvspKSEpiamkIikdS5TYQQUlc0x4oQQjSHCistN3r0aE03QeWcnZ0hlUqRk5Oj1OM5jsODBw/wxhtvAFCusKott+fPn6Nx48YIDg7GyZMnlWpHdYqLi3VqfhWgm+eculB27Cg74arLjHqslEPnGzvKjh1lJ5zYMqPCSstlZWVpugkqJ1tBUtnC6sWLF3j58iVat24NAEoNBawtt4KCAlhaWiI4OBiXLl1i7gWT9VjpEl0859SFsmNH2QlXXWaywkoqlaq7OaJC5xs7yo4dZSec2DKjwkrLHT16VNNNUDlbW1sAyhdWsoUrhAwFrC23wsJCWFhYoFu3bnj16hXOnj2rVFtep4s9Vrp4zqkLZceOshOuusxkQwFLS0vV3RxRofONHWXHjrITTmyZUWFF1E7WYyW7D1ptduzYAQMDA/j6+gJQzRwrWY+Vj48P7O3tBc2zKisrw3/+8x+UlpbqZI8VIUS8ZD1WZWVlGm4JIYToHyqsiNrV1GN14MABzJ49G8XFxSgtLcW2bduwcOFC/PDDD3BycoKpqWmVwur999+Hm5uboDbICisDAwN07dpV0DyrY8eO4YMPPkBCQoJO9lgRQsTLxsYGQMXcVEIIIeql9HLrRDPCwsI03QSVs7GxgUQiqdJj9eLFCwwYMAAAcO7cOdy8eRPl5eWYMGECPvvsMwCAhYVFlTlW//3vfwFUzCmQ3RSzttwKCwthaWkJAAgODsZ3332HV69ewcio9reEbNjg06dPUVRUpHOFlS6ec+pC2bGj7ISrLrOPP/4YFhYWCA4O1kCLxIPON3aUHTvKTjixZUY9VlpO9se/LjEwMICNjU2VHqv//Oc//Pfnz59HQUEB2rZti1WrVvHLmVtaWiI7O7vaidmpqan897XlVlBQAAsLCwBAp06dUFBQgNu3byvV/jNnzgAA0tPT8fz5czRo0ECp54mFLp5z6kLZsaPshKsuM3Nzc3z00Uf8h0ykenS+saPs2FF2woktM7ryarldu3Zpugn1wtbWVq6wKiwsxB9//IHhw4fz277++mscOXJErkfI3NwcixYtwvvvv89vc3R0BADcvHmT31ZTbhzH8UMBAcDd3R1ARQ9UbTiOk+uxevbsGRo2bFjr88REV885daDs2FF2wlFm7Cg7dpQdO8pOOLFlRoUV0Qg7Ozu5oYDr1q1DdnY2Fi9eDHNzcwDAyJEj+fkCMsnJyQCA3377DadOnQLwz2TtGzduKPXaJSUl4DiOL6waNWoEoKIHqjZ3797FixcvYGRkhPT0dJ0srAghhBBCiHBUWBGNsLOz43usysvLsWTJEowYMQJeXl5o1qwZDA0N0bx5c4XPDwoKwrRp01BcXIxnz54BAE6dOqXUhG3Z4heywsrCwgLW1tbIyMio9bmyYYAhISF8YaVrQwEJIYQQQohwtHiFluvUqZOmm1AvbG1t+R6rffv24e7du9i4cSMAoEWLFigpKeF7oir79ttvUVpaitGjR8Pf3x+ff/45Xr16hQEDBmDfvn34/fffMWfOnBpzkxVWsjlWQEWvlTI9VmfPnkWLFi3g4+OD2NhY5OTk6FyPla6ec+pA2bGj7ISjzNhRduwoO3aUnXBiy4wKKy3XunVrTTehXtjZ2eH+/fsAgCVLliA4OBhBQUEAgLlz5+L58+fVPu/LL7/kv//ss8/www8/AAA++eQTtGzZEu+//z6aN2+Ovn37Knzt13usAMDZ2VnpHqtOnTrB2dkZt27dAgCdK6x09ZxTB8qOHWUnHGXGjrJjR9mxo+yEE1tmNBRQy0VGRmq6CfVCNhSwuLgYp0+fRkREBL+vffv26NOnT63HmD17Nv+9k5MTfvrpJ4SHh2PMmDF8wVUd2XLtlQsrZXqsioqKcOXKFXTq1AkuLi78dl0rrHT1nFMHyo4dZSccZcaOsmNH2bGj7IQTW2ZUWBGNsLOzw7Nnz5CUlITy8nL4+fkJPoazszP/fcOGDWFoaIjNmzfD3d0dv/32W5X7XckoGgpYU49Veno6du7ciVevXiEoKAgtWrSQe21CCCGEEKLfqLAiGtGpUydkZGRg27ZtAIA33niD6Tienp4AAAcHBwAVNx/etGkTnj17hgULFuDPP//EmTNn+GGHd+7cwaxZswBUHQpYU4/VW2+9hYkTJ0IikcDX11duzC8VVoQQQgghhOZYaTmxjS1VVs+ePWFhYYFFixahadOmsLa2ZjrO8ePHERsbK3czTF9fXzg6OuL777+HsbExzMzMYGdnhwsXLmD16tW4fv06gKqF1bNnz1BWVgZjY2O513j27BliYmIAVNzH6vX9rG3XVrp6zqkDZceOshOOMmNH2bGj7NhRdsKJLTPqsdJyXbp00XQT6oWZmRkGDhwIoG5vGnd3d0ydOlVum0Qi4RevKCsrw8uXL1FUVIRRo0YhNjaWf1zlwsrHxwccx/FFV2VRUVEAgHnz5mHHjh389rNnz2LevHmQSCTM7ddGunrOqQNlx46yE44yY0fZsaPs2FF2woktMyqstFzlP+R1zZ9//olffvkFX331lcqP7eLigqZNm2Lw4MEYOnQodu/ejYSEBFy6dIl/TOWeJ39/fxgZGSEhIaHKsS5fvow33ngD3333HUaOHMlvDwwMxHfffafytmuaLp9z9Y2yY0fZCUeZsaPs2FF27Cg74cSWGRVWWi4vL0/TTag39vb2+PDDD+vlHgU+Pj64f/8+du3ahe3bt6Nr1674/fff5XqpKvc0mZubo127dvwNgCtLTk5Gs2bNVN5GbaXL51x9o+zYUXbCUWbsKDt2lB07yk44sWVGhRXRaYaGhjAyqphKOGPGDIX3xwIqFtSIj48Hx3Fy25OTk9G8efN6bSchhBBCCBE3Kqy0XOPGjTXdBFFSlJuZmRlmz55d7YIT/fr1w/3793Hz5k1+W0lJCdLS0vSqsKJzjh1lx46yE44yY0fZsaPs2FF2woktMwn3+sfzBHl5ebC1tUVubi5sbGw03RyiJsXFxWjYsCE+++wzzJs3DwCQlJQEHx8fHD9+HN27d9dwCwkhhBBCiLaiHistJ1vmmwjDkpuZmRnCwsJw+PBhftudO3cAQK96rOicY0fZsaPshKPM2FF27Cg7dpSdcGLLjAorLffo0SNNN0GUWHNr27Ytbt++zf/8999/w83NDS4uLqpqmtajc44dZceOshOOMmNH2bGj7NhRdsKJLTMqrAippEWLFsjMzEROTg4A4ODBg+jfv7/O3auKEEIIIYSolpGmG0BqVnl5cKI81txatGgBoGIlwIKCAty5cweLFi1SZdO0Hp1z7Cg7dpSdcJQZO8qOHWXHjrITTmyZ0eIV1aDFK/RXfn4+bGxsMGnSJGzfvh2BgYGIiYmBqamppptGCCGEEEK0GA0F1HJnz57VdBNEiTU3a2truLi4YN26dejbty8OHTqkd0UVnXPsKDt2lJ1wlBk7yo4dZceOshNObJlRYaXlrl+/rukmiFJdchs7dixmz56NnTt3wszMTIWtEgc659hRduwoO+EoM3aUHTvKjh1lJ5zYMqM5VoS8ZsmSJZpuAiGEEEIIERnqsSKEEEIIIYSQOqLFK6qhTYtXlJWVwdjYWKNtECPKjR1lx46yY0fZCUeZsaPs2FF27Cg74cSWGfVYabmUlBRNN0GUKDd2lB07yo4dZSccZcaOsmNH2bGj7IQTW2ZUWGm5U6dOaboJokS5saPs2FF27Cg74SgzdpQdO8qOHWUnnNgy06rCKi4uDoMGDULjxo0hkUiwe/fuKo9JSkrC4MGDYWtrC0tLSwQEBCAtLY3fX1xcjFmzZsHR0RFWVlYYMWIEMjIy1PhbEEIIIYQQQvSNVhVWBQUF8PPzw7Jly6rdn5KSguDgYLRq1QrHjx/H1atX8eWXX8otif3BBx9g37592LFjB06cOIEnT55g+PDh6voVCCGEEEIIIXpIaxevkEgkiIqKwtChQ/ltY8eOhbGxMTZs2FDtc3Jzc9GwYUNs3rwZI0eOBADcunULrVu3RkJCAjp16qTUa2vT4hXPnz9HgwYNNNoGMaLc2FF27Cg7dpSdcJQZO8qOHWXHjrITTmyZaVWPVU2kUin279+PFi1aICwsDE5OTggKCpIbLnjx4kWUlZWhd+/e/LZWrVrB3d0dCQkJCo9dUlKCvLw8uS9tUVZWpukmiBLlxo6yY0fZsaPshKPM2FF27Cg7dpSdcGLLTDQ3CM7MzMTLly+xcOFCfP/991i0aBEOHTqE4cOH4++//0b37t2Rnp4OExMT2NnZyT23UaNGSE9PV3jsBQsW4Jtvvqmyff369TA3NwcAjBs3Dk+fPsXx48f5/f3794exsTH27NnDb+vatSu8vb2xfv16flubNm0QFBSErVu3oqCgAADg5uaGsLAwHDx4EE+ePAEA2NjYYNSoUTh9+jSSkpL43/uzzz5DUlISzpw5wx9z+PDhKCgoQExMDL+tV69ecHR0xPbt2/ltHTt2hJ+fHyIjIyGVSgEAzZs3R0hICKKiovDixQsAgJOTEwYNGoSjR48iNTUVAGBqaoqIiAhcvHgRly9f5o85fvx4PH78GCdOnOC3DRgwAIaGhti7dy+/LTg4GJ6ennI9jL6+vggMDMSWLVtQWFgIAHB3d0efPn2wf/9+/t/J1tYWI0eORHx8PG7fvs0//6233sK1a9dw7tw5ftvIkSORl5eHw4cP89tKSkoQERGBHTt28NsCAgLQtm1brFmzBrKO2hYtWqBbt27466+/kJOTA6DifBk4cCBiY2Px4MEDAICZmRkmTJiA8+fP4+rVq/wxIyIikJaWhri4OH7bwIEDAQDR0dH8tpCQELi7u2Pjxo38trZt2yIgIACbNm1CcXExAMDDwwO9e/dGdHQ0PzfQzs4OI0aMwMmTJ3Hnzh0AFT26U6dOxdWrV3H+/Hn+mKNGjUJ2djZiY2P5bX379oWNjQ127tzJbwsMDISvry9Wr17Nb2vZsiWCg4OxYcMGODo6AgCcnZ0xYMAAHDlyhJ/LaGFhgXHjxuHcuXO4du0a//w333wT9+/fR3x8PL9t8ODBKC8vx/79+/lt3bt3h6urKzZv3sxva9euHTp06ICNGzeipKQEANC0aVP06tUL+/btQ2ZmJgDAwcEBw4YNQ1xcHJKTkwEABgYGmDJlCq5cuYILFy7wxxw9ejSysrJw9OhRfltYWBgsLS2xa9cuflunTp3QunVrREZG8ttat26NLl26YMeOHfwHLY0bN0Z4eDhiYmLw6NEjAIClpSXGjh2Ls2fP4vr168jMzISTkxMmTpyIlJQUuUm3Q4YMQVlZGQ4cOMBvCw0NhYuLC7Zs2cJva9++Pfz9/bF+/Xr+PxQvLy/06NEDe/bswfPnzwEAjo6OGDp0KI4fP86vmmRkZIRJkyYhMTERly5d4o85duxYZGZm4tixY/y2fv36wdzcHFFRUfy2zp07o2XLlli7di2/zcfHB507d8a2bdvw8uVLAICrqyv69euHQ4cO4fHjxwAAKysrjBkzBgkJCbh58yb//MmTJ+P27dtyH24NGzYMRUVFOHToEL+tuLgYkydPxtatW/lt/v7+aN++PdatW4dXr14BALy9vREaGordu3cjKysLANCgQQMMGTIEf//9N+7duwcAMDY2xsSJE3Hp0iUkJibyx9TUtRwApkyZotJreV5eHj744AOdvpb37t0b9vb2Kr+Wb9++HVZWVvwxdfFavnPnTuTm5gJQ7bVcdp3T5Wu5jKqv5bm5ufjwww91+lres2dPODk5qexa/uzZM3z++edacS1/6623UCtOSwHgoqKi+J8fP37MAeDGjRsn97hBgwZxY8eO5TiO4zZt2sSZmJhUOVZAQAD36aefKnyt4uJiLjc3l/96+PAhB4DLzc1VzS9TB6tWrdJ0E0SJcmNH2bGj7NhRdsJRZuwoO3aUHTvKTjixZSaaHqsGDRrAyMgIPj4+cttbt27Nf6ri7OyM0tJS5OTkyPVaZWRkwNnZWeGxTU1NYWpqWi/tJoQQQgghhOg+0cyxMjExQUBAgNxQAgC4c+cOPDw8AAAdOnSAsbGxXHfx7du3kZaWhs6dO6u1vaoSGhqq6SaIEuXGjrJjR9mxo+yEo8zYUXbsKDt2lJ1wYstMq3qsXr58ibt37/I/379/H5cvX4aDgwPc3d3xySefYMyYMQgJCUGPHj1w6NAh7Nu3jx9faWtri7feegsffvghHBwcYGNjgzlz5qBz585KrwiobVxcXDTdBFGi3NhRduwoO3aUnXCUGTvKjh1lx46yE05smWlVj9WFCxfQvn17tG/fHgDw4Ycfon379vjqq68AVEyS+/PPP/HTTz/B19cXq1atwl9//YXg4GD+GEuXLsXAgQMxYsQIhISEwNnZWW5yo9hUnghJlEe5saPs2FF27Cg74SgzdpQdO8qOHWUnnNgy06oeq9DQUH6FH0WmTp2KqVOnKtxvZmaGZcuWKbzJMCGEEEIIIYSomlYVVtpCVtxpw/2sioqKtKIdYkO5saPs2FF27Cg74SgzdpQdO8qOHWUnnLZlZm1tDYlEonC/hKuti0gPPXr0CE2aNNF0MwghhBBCCCFaIjc3FzY2Ngr3U2FVDalUiidPntRalda3vLw8NGnSBA8fPqzxH5HIo9zYUXbsKDt2lJ1wlBk7yo4dZceOshNOGzOrrTagoYDVMDAwgJubm6abwbOxsdGaE0pMKDd2lB07yo4dZSccZcaOsmNH2bGj7IQTU2ZatSogIYQQQgghhIgRFVaEEEIIIYQQUkdUWGkxU1NTzJ8/H6ampppuiqhQbuwoO3aUHTvKTjjKjB1lx46yY0fZCSfGzGjxCkIIIYQQQgipI+qxIoQQQgghhJA6osKKEEIIIYQQQuqICitCCCGEEEIIqSMqrAghhBBCCCGkjqiwEmjBggUICAiAtbU1nJycMHToUNy+fVvuMcXFxZg1axYcHR1hZWWFESNGICMjg99/5coVjBs3Dk2aNIG5uTlat26N//73vwpf89SpUzAyMkK7du1qbR/Hcfjqq6/g4uICc3Nz9O7dG8nJyXKP+eGHH9ClSxdYWFjAzs5O0O9fF7qQnUxJSQnatWsHiUSCy5cvK/X7sxJ7bsePH4dEIqn26/z588IDEUDbs9u1axf69u0LR0dHhedSbe2rL+rKTtH5kZ6eXmP7tPVapwu5yejida6+ctOH6xxrdnSdq1BSUoK5c+fCw8MDpqamaNq0KdasWVNrG5ctW4amTZvCzMwMQUFBOHfunNz+//3vfwgNDYWNjQ0kEglycnLYwhBAF3KT4TgO4eHhkEgk2L17t7AgFByQCBAWFsZFRkZy169f5y5fvsz179+fc3d3516+fMk/5p133uGaNGnCHT16lLtw4QLXqVMnrkuXLvz+1atXc++99x53/PhxLiUlhduwYQNnbm7O/fbbb1VeLzs7m/Py8uL69u3L+fn51dq+hQsXcra2ttzu3bu5K1eucIMHD+Y8PT25oqIi/jFfffUVt2TJEu7DDz/kbG1t65SHELqQncx7773HhYeHcwC4xMREpjyUJfbcSkpKuKdPn8p9TZs2jfP09OSkUmndA6qBtme3fv167ptvvuFWrlyp8FyqrX31RV3Z/f333xwA7vbt23LnSHl5eY3t09ZrnS7kJqOL17n6yk0frnOs2dF1rsLgwYO5oKAg7siRI9z9+/e506dPc/Hx8TW2b+vWrZyJiQm3Zs0a7saNG9z06dM5Ozs7LiMjg3/M0qVLuQULFnALFizgAHDZ2dmqCacGupCbzJIlS/jrXFRUVN2C4TiOCqs6yszM5ABwJ06c4DiO43JycjhjY2Nux44d/GOSkpI4AFxCQoLC47z77rtcjx49qmwfM2YMN2/ePG7+/Pm1/qEmlUo5Z2dnbvHixfy2nJwcztTUlNuyZUuVx0dGRqq1sHqdWLM7cOAA16pVK+7GjRtq+YPjdWLNTaa0tJRr2LAh9+2339Z47PqgTdlVdv/+/WrPJdb21Yf6yk72x5qQPwbEdK0Ta266ep1Tx/nGcbp5nWPJrjJ9vs4dPHiQs7W15bKysgS1JzAwkJs1axb/c3l5Ode4cWNuwYIFVR5b13+fuhBrbomJiZyrqyv39OlTlRVWNBSwjnJzcwEADg4OAICLFy+irKwMvXv35h/TqlUruLu7IyEhocbjyI4hExkZiXv37mH+/PlKteX+/ftIT0+Xe21bW1sEBQXV+NqaIsbsMjIyMH36dGzYsAEWFhZKHVvVxJhbZXv37kVWVhamTJmi1GuokjZlpwzW9tWH+swOANq1awcXFxf06dMHp06dqrEtYrrWiTE3Xb/OAfV/vunqdQ4Qlp0y9OE6t3fvXnTs2BE//fQTXF1d0aJFC3z88ccoKipSeIzS0lJcvHhR7rUNDAzQu3dvvbnO1WduhYWFGD9+PJYtWwZnZ2fhv7QCRio7kh6SSqV4//330bVrV7Rp0wYAkJ6eDhMTkyrj+Rs1aqRwHPLp06exbds27N+/n9+WnJyMzz//HCdPnoSRkXL/TLLjN2rUSOnX1hQxZsdxHCZPnox33nkHHTt2RGpqqlLHViUx5va61atXIywsDG5ubkq9hqpoW3bKYGlffajP7FxcXPDnn3+iY8eOKCkpwapVqxAaGoqzZ8/C39+/2uOI5Vonxtx0/TqnrvNNF69zLNkpQx+uc/fu3UN8fDzMzMwQFRWF58+f491330VWVhYiIyOrPc7z589RXl5e7Xl369atOvymqiXW3D744AN06dIFQ4YMYfm1FaLCqg5mzZqF69evIz4+nvkY169fx5AhQzB//nz07dsXAFBeXo7x48fjm2++QYsWLap93qZNm/D222/zPx88eBCGhobM7VA3MWb322+/IT8/H//+97+Z21xXYsytskePHiEmJgbbt29nbj8rbcuuW7duzO1Qt/rKDgBatmyJli1b8j936dIFKSkpWLp0KTZs2CDqa50Yc9Pl6xygnvNNF69zAFt2dJ2rIJVKIZFIsGnTJtja2gIAlixZgpEjR+KPP/7AhQsXEB4ezj9+xYoV6NGjB/svo0ZizG3v3r04duwYEhMTmdusCBVWjGbPno3o6GjExcXJfSLl7OyM0tJS5OTkyFXqGRkZVboab968iV69emHGjBmYN28evz0/Px8XLlxAYmIiZs+eDaDi5OI4DkZGRjh8+DAGDx6MoKAg/jmurq54+vQp/1ouLi5yr63MCmXqItbsjh07hoSEBJiamsq1pWPHjpgwYQLWrVtXt2BqIdbcKouMjISjoyMGDx5cpyyE0sbslCGkffWlPrNTJDAwkP9PWqzXOrHmpsvXOUVUfb7p4nVOkdqyU4Y+XOdcXFzg6urKFwcA0Lp1a3Ach0ePHqFjx45yqyU2atQIpqamMDQ0rLI6ojpzqY1Yczt27BhSUlKq9KiNGDEC3bp1w/HjxxnS+H91nqWlZ6RSKTdr1iyucePG3J07d6rsl03Y27lzJ7/t1q1bVSbsXb9+nXNycuI++eSTKscoLy/nrl27Jvc1c+ZMrmXLlty1a9fkVl15vW3Ozs7czz//zG/Lzc3VmgndYs/uwYMHcseNiYnhAHA7d+7kHj58yJxLbcSeW+XHenp6ch999JHgDFhpc3aV1Tapu7b21Qd1ZKdI7969uWHDhtXYNm291ok9N12+zimiyvNNV69zitSWXWX6fJ1bsWIFZ25uzuXn5/Pbdu/ezRkYGHCFhYUK2xcYGMjNnj2b/7m8vJxzdXXV+OIVYs/t6dOnVf7fBsD997//5e7du6d8ENWgwkqgmTNncra2ttzx48fllhut/A/8zjvvcO7u7tyxY8e4CxcucJ07d+Y6d+7M77927RrXsGFDLiIiQu4YmZmZCl9X2VXGFi5cyNnZ2XF79uzhrl69yg0ZMqTKUroPHjzgEhMTuW+++YazsrLiEhMTucTERLkTtz7oQnaVKfpPQtV0JbfY2FgOAJeUlCQ8BEbanl1WVhaXmJjI7d+/nwPAbd26lUtMTOSePn2qdPvqi7qyW7p0Kbd7924uOTmZu3btGvevf/2LMzAw4GJjY2tsn7Ze63Qht8p07TpX37np8nWONTu6znFcfn4+5+bmxo0cOZK7ceMGd+LECa558+bctGnTamzf1q1bOVNTU27t2rXczZs3uRkzZnB2dnZceno6/5inT59yiYmJ/HL2cXFxXGJiouCV9ITQhdxeB1puXTMAVPsVGRnJP6aoqIh79913OXt7e87CwoIbNmyY3AVk/vz51R7Dw8ND4esq+4eaVCrlvvzyS65Ro0acqakp16tXL+727dtyj5k0aVK1r//3338LTEMYXciuMnX9waEruY0bN04t9yWpTNuzi4yMrPbY8+fPV7p99UVd2S1atIjz9vbmzMzMOAcHBy40NJQ7duxYre3T1mudLuRWma5d5+o7N12+zrFmR9e5CklJSVzv3r05c3Nzzs3Njfvwww9r7HWR+e233zh3d3fOxMSECwwM5M6cOSO3X9HrV/4dVE0Xcqvud1JFYSX5/4MRQgghhBBCCGFE97EihBBCCCGEkDqiwooQQgghhBBC6ogKK0IIIYQQQgipIyqsCCGEEEIIIaSOqLAihBBCCCGEkDqiwooQQgghhBBC6ogKK0IIIYQQQgipIyqsCCGEEAW+/vprSCQSPH/+XNNNIYQQouWosCKEECIqa9euhUQiqfbr888/13TzCCGE6CkjTTeAEEIIYfHtt9/C09NTblubNm001BpCCCH6jgorQgghohQeHo6OHTtquhmEEEIIABoKSAghRAcdPHgQ3bp1g6WlJaytrTFgwADcuHGjyuNu3bqF0aNHo2HDhjA3N0fLli0xd+7cKo/LycnB5MmTYWdnB1tbW0yZMgWFhYVyj4mMjETPnj3h5OQEU1NT+Pj4YPny5VWOdeHCBYSFhaFBgwYwNzeHp6cnpk6dqrpfnhBCiEZQjxUhhBBRys3NrbKoRIMGDbBhwwZMmjQJYWFhWLRoEQoLC7F8+XIEBwcjMTERTZs2BQBcvXoV3bp1g7GxMWbMmIGmTZsiJSUF+/btww8//CB33NGjR8PT0xMLFizApUuXsGrVKjg5OWHRokX8Y5YvX4433ngDgwcPhpGREfbt24d3330XUqkUs2bNAgBkZmaib9++aNiwIT7//HPY2dkhNTUVu3btqt+wCCGE1DsJx3GcphtBCCGEKGvt2rWYMmVKtfvy8/PRpEkTjBo1Cv/73//47RkZGWjZsiVGjx7Nb+/evTsSExNx/fp1uLu784/lOA4SiQRAxaqA33zzDaZOnYrVq1fzjxk+fDji4uLkCruioiKYm5vLtadfv35ITk5GSkoKAGD37t0YNmwYzp8/T8MYCSFEx1CPFSGEEFFatmwZWrRoIbftyL799qYAAAOXSURBVJEjyMnJwbhx4+SKHkNDQwQFBeHvv/8GADx79gxxcXH417/+JVdUAeCLqsreeecduZ+7deuGqKgo5OXlwcbGBgDkiqrc3FyUlZWhe/fuiImJQW5uLmxtbWFnZwcAiI6Ohp+fH4yNjdkDIIQQolWosCKEECJKgYGBVXp9fvrpJwBAz549q32OrAi6d+8eAOVXEXy9+LK3twcAZGdn88c8deoU5s+fj4SEhCrzr2SFVffu3TFixAh88803WLp0KUJDQzF06FCMHz8epqamSrWFEEKIdqLCihBCiM6QSqUAgA0bNsDZ2bnKfiMjtv/2DA0Nq90uG02fkpKCXr16oVWrVliyZAmaNGkCExMTHDhwAEuXLuXbJZFIsHPnTpw5cwb79u1DTEwMpk6dil9++QVnzpyBlZUVU/sIIYRoHhVWhBBCdIa3tzcAwMnJCb1791b4OC8vLwDA9evXVfK6+/btQ0lJCfbu3SvXuyUbevi6Tp06oVOnTvjhhx+wefNmTJgwAVu3bsW0adNU0h5CCCHqR8utE0II0RlhYWGwsbHBjz/+iLKysir7nz17BgBo2LAhQkJCsGbNGqSlpck9hmVNJ1mPVuXn5ubmIjIyUu5x2dnZVY7frl07AEBJSYng1yWEEKI9qMeKEEKIzrCxscHy5cvx5ptvwt/fH2PHjkXDhg2RlpaG/fv3o2vXrvj9998BAL/++iuCg4Ph7++PGTNmwNPTE6mpqdi/fz8uX74s6HX79u0LExMTDBo0CG+//TZevnyJlStXwsnJCU+fPuUft27dOvzxxx8YNmwYvL29kZ+fj5UrV8LGxgb9+/dXZRSEEELUjAorQgghOmX8+PFo3LgxFi5ciMWLF6OkpASurq7o1q2b3DLtfn5+OHPmDL788kssX74cxcXF8PDwwOjRowW/ZsuWLbFz507MmzcPH3/8MZydnTFz5kw0bNhQ7ua/3bt3x7lz57B161ZkZGTA1tYWgYGB2LRpEzw9PVXy+xNCCNEMuo8VIYQQQgghhNQRzbEihBBCCCGEkDqiwooQQgghhBBC6ogKK0IIIYQQQgipIyqsCCGEEEIIIaSOqLAihBBCCCGEkDqiwooQQgghhBBC6ogKK0IIIYQQQgipIyqsCCGEEEIIIaSOqLAihBBCCCGEkDqiwooQQgghhBBC6ogKK0IIIYQQQgipIyqsCCGEEEIIIaSOqLAihBBCCCGEkDr6Pxahp5Go1JvqAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Métodos de promedios móviles\n",
        "\n",
        "**Ejercicio 1**: Aplica una media móvil simple (SMA) a la serie de tiempo. Prueba con distintos tamaños de ventana (`window`) y selecciona uno que consideres adecuado. Justifica tu elección con base en el comportamiento observado en la serie.\n",
        "\n",
        "Ten en cuenta que la serie de tiempo no incluye sábados ni domingos; por lo tanto, aproximadamente:\n",
        "\n",
        "+ 5 observaciones corresponden a una semana\n",
        "+ 21 observaciones a un mes\n",
        "+ 252 observaciones a un año\n",
        "\n",
        "Una vez termines, borra estas instrucciones y redacta tus observaciones.\n"
      ],
      "metadata": {
        "id": "DdiVRetVw9br"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "mphRfQpXzDbT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Método de suavisación exponencial\n",
        "\n",
        "**Ejercicio 2**: Aplica una suavización exponencial simple (SES) a la serie de tiempo. Prueba con distintos valores del parámetro de suavizamiento (por ejemplo, mediante span o alpha) y selecciona uno que consideres adecuado. Justifica tu elección con base en el comportamiento observado en la serie.\n",
        "\n",
        "Ten en cuenta que la serie de tiempo no incluye sábados ni domingos; por lo tanto, aproximadamente:\n",
        "\n",
        "+ 5 observaciones corresponden a una semana\n",
        "+ 21 observaciones a un mes\n",
        "+ 252 observaciones a un año\n",
        "\n",
        "Una vez termines, borra estas instrucciones y redacta tus observaciones."
      ],
      "metadata": {
        "id": "qtw9ZBg4zD52"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "zlBunu0pzsOp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Ejercicio 3**: Observando las curvas por SMA y SES, señala las ventajas y desventajas que puedes observar en ambos gráficos.\n",
        "\n",
        "Una vez termines, borra estas instrucciones y redacta tus observaciones."
      ],
      "metadata": {
        "id": "tqG896-izssc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Tendencias no lineales"
      ],
      "metadata": {
        "id": "J51BFOIlEY-7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Ejercicio 4**: Realiza una regresión polinomial de grado 2. Usa series de Fourier para extraer la estacionalidad y calcular el ruido de medición. Apóyate en los gráficos correspondientes y analiza las longitudes de onda para establecer si existe estacionalidad. Ten en cuenta que la serie de tiempo no incluye sábados ni domingos; por lo tanto, aproximadamente:\n",
        "\n",
        "+ 5 observaciones corresponden a una semana\n",
        "+ 21 observaciones a un mes\n",
        "+ 252 observaciones a un año\n",
        "\n",
        "Una vez termines, borra estas instrucciones y redacta tus observaciones."
      ],
      "metadata": {
        "id": "WdrM5KdbEpBD"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "tuUqs6MXGjkF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Análisis de los componentes de la serie\n",
        "\n",
        "**Ejercicio 5**: Apóyate de los gráficos correspondientes para analizar cada uno de los componentes de la serie por separado. Comenta lo que se puede observar de cada componente, si crees que se pudo aproximar bien o no, y por qué.\n",
        "\n",
        "Una vez termines, borra estas instrucciones y redacta tus observaciones."
      ],
      "metadata": {
        "id": "1YR0KlZ0Gutn"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "wBcCC1ndHcWZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Análisis fundamental (ligero)"
      ],
      "metadata": {
        "id": "Zk2BqsHAJk8d"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Ejercicio 6**: Realiza una interpretación de los componentes de la serie de tiempo (tendencia, estacionalidad y ruido).\n",
        "\n",
        "En tu análisis:\n",
        "\n",
        "+ Explica qué factores externos podrían justificar la tendencia observada (por ejemplo: crecimiento de la empresa, cambios en el mercado, decisiones estratégicas, etc.).\n",
        "+ Identifica posibles eventos o situaciones que expliquen los patrones de estacionalidad.\n",
        "+ Reflexiona sobre el ruido, indicando qué tipo de eventos inesperados o aleatorios podrían estar representados en este componente.\n",
        "\n",
        "Este análisis no requiere un estudio exhaustivo del entorno económico, pero sí una interpretación razonada, similar a un análisis fundamental básico.\n",
        "\n",
        "Una vez termines, borra estas instrucciones y redacta tus observaciones."
      ],
      "metadata": {
        "id": "DuCXXSVAJnVG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Aplicaciones\n",
        "\n",
        "**Ejercicio 7**: Analiza qué personas, empresas o instituciones podrían beneficiarse del análisis realizado.\n",
        "\n",
        "En tu respuesta:\n",
        "\n",
        "+ Menciona al menos tres actores (por ejemplo: inversionistas, empresas, instituciones financieras, gobierno, etc.).\n",
        "+ Explica cómo utilizarían este tipo de análisis.\n",
        "+ Describe qué beneficios concretos podrían obtener.\n",
        "\n",
        "Adicionalmente, reflexiona sobre cómo un análisis más profundo podría mejorar estos beneficios o ampliar sus aplicaciones.\n",
        "\n",
        "Relaciona tu respuesta con los resultados obtenidos en tu análisis (tendencia, estacionalidad y ruido).\n",
        "\n",
        "Una vez termines, borra estas instrucciones y redacta tus observaciones."
      ],
      "metadata": {
        "id": "hW08iaowHctt"
      }
    }
  ]
}
